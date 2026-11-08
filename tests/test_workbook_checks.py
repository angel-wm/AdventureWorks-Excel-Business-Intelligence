"""Synthetic contracts: no Excel session, downloaded data or workbook mutation."""
import copy
import datetime as dt
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.workbook_checks import (
    EXPECTED_SHEETS, HIDDEN_SHEETS, MONTH_HEADERS, RFM_HEADERS,
    check_monthly_output, check_rfm_output, handoff_matches, package_failures,
)


def customer_fixture():
    expected = {
        10: dict(date=dt.date(2025, 6, 1), recency=28, frequency=3,
                 sales=Decimal('100.25'), R=5, F=3, M=3, segment='Frequent'),
        20: dict(date=dt.date(2025, 5, 1), recency=59, frequency=1,
                 sales=Decimal('25.00'), R=5, F=1, M=1, segment='Recent'),
    }
    cells = {col + '5': value for col, value in RFM_HEADERS.items()}
    # Deliberately literal outputs, independent of the production row builder.
    for row, values in [(6, [10, 45809, 28, 3, 100.25, 5, 3, 3, 'Frequent']),
                        (7, [20, 45778, 59, 1, 25.0, 5, 1, 1, 'Recent'])]:
        cells.update({col + str(row): value for col, value in zip('ABCDEFGHI', values)})
    return cells, expected


def monthly_fixture():
    return ({'A4': 'Order month', 'B4': 'Shipped sales',
             'A5': 45658, 'B5': 100.25, 'A6': 45689, 'B6': 25.0},
            {'2025-01': Decimal('100.25'), '2025-02': Decimal('25.00')})


def copy_row(cells, columns, source, target):
    for column in columns:
        cells[column + str(target)] = cells[column + str(source)]


class CustomerOutputTests(unittest.TestCase):
    def setUp(self):
        self.cells, self.expected = customer_fixture()

    def check(self):
        return check_rfm_output(self.cells, self.expected)

    def test_complete_valid_population(self):
        result = self.check()
        self.assertTrue(result['passed'], result)
        self.assertEqual(result['rows_compared'], 2)

    def test_extra_customer_including_after_gap(self):
        for row in (8, 1000):
            with self.subTest(row=row):
                cells = self.cells.copy()
                copy_row(cells, RFM_HEADERS, 6, row)
                cells['A' + str(row)] = 99
                result = check_rfm_output(cells, self.expected)
                self.assertFalse(result['passed'])
                self.assertEqual(result['unexpected_customers'], [99])
                self.assertEqual(result['rows_compared'], 3)

    def test_duplicate_customer_including_after_gap(self):
        for row in (8, 1000):
            with self.subTest(row=row):
                cells = self.cells.copy()
                copy_row(cells, RFM_HEADERS, 6, row)
                result = check_rfm_output(cells, self.expected)
                self.assertFalse(result['passed'])
                self.assertEqual(result['duplicate_customers'], [10])

    def test_missing_customer(self):
        for column in RFM_HEADERS:
            del self.cells[column + '7']
        result = self.check()
        self.assertFalse(result['passed'])
        self.assertEqual(result['missing_customers'], [20])

    def test_data_without_id_is_rejected_after_gap(self):
        self.cells['E1000'] = 123
        result = self.check()
        self.assertFalse(result['passed'])
        self.assertEqual(result['invalid_id_rows'], [1000])

    def test_internal_gap_is_rejected(self):
        copy_row(self.cells, RFM_HEADERS, 7, 8)
        for column in RFM_HEADERS:
            del self.cells[column + '7']
        result = self.check()
        self.assertFalse(result['passed'])
        self.assertFalse(result['contiguous_rows'])

    def test_header_errors(self):
        for column in RFM_HEADERS:
            with self.subTest(column=column):
                cells = self.cells.copy()
                cells[column + '5'] = 'Unexpected heading'
                result = check_rfm_output(cells, self.expected)
                self.assertFalse(result['passed'])
                self.assertIn(column, result['header_errors'])

    def test_each_customer_value_is_checked(self):
        for column in 'BCDEFGHI':
            with self.subTest(column=column):
                cells = self.cells.copy()
                cells[column + '6'] = 'Wrong' if column == 'I' else -999
                result = check_rfm_output(cells, self.expected)
                self.assertFalse(result['passed'])
                self.assertEqual(result['mismatches'][0]['column'], column)

    def test_invalid_ids(self):
        for value in (None, '', '10', True, 0, -1, 1.5, float('nan'), float('inf')):
            with self.subTest(value=value):
                self.cells['A6'] = value
                self.assertFalse(self.check()['passed'])

    def test_nonfinite_and_missing_amounts(self):
        for value in (None, '', '100.25', True, float('nan'), float('inf')):
            with self.subTest(value=value):
                self.cells['E6'] = value
                self.assertFalse(self.check()['passed'])

    def test_amount_tolerance(self):
        self.cells['E6'] = 100.254
        self.assertTrue(self.check()['passed'])
        self.cells['E6'] = 100.256
        self.assertFalse(self.check()['passed'])

    def test_empty_formatted_cells_do_not_create_rows(self):
        self.cells.update({'A1000': None, 'I2000': '', 'J3000': 'Outside output'})
        self.assertTrue(self.check()['passed'])


class MonthlyOutputTests(unittest.TestCase):
    def setUp(self):
        self.cells, self.expected = monthly_fixture()

    def check(self):
        return check_monthly_output(self.cells, self.expected)

    def test_complete_valid_population(self):
        result = self.check()
        self.assertTrue(result['passed'], result)
        self.assertEqual(result['rows_compared'], 2)

    def test_extra_month_including_after_gap(self):
        for row in (7, 1000):
            with self.subTest(row=row):
                cells = self.cells.copy()
                cells['A' + str(row)] = 45717  # March 1, 2025
                cells['B' + str(row)] = 1
                result = check_monthly_output(cells, self.expected)
                self.assertFalse(result['passed'])
                self.assertEqual(result['unexpected_months'], ['2025-03'])

    def test_duplicate_month_including_after_gap(self):
        for row in (7, 1000):
            with self.subTest(row=row):
                cells = self.cells.copy()
                copy_row(cells, MONTH_HEADERS, 5, row)
                result = check_monthly_output(cells, self.expected)
                self.assertFalse(result['passed'])
                self.assertEqual(result['duplicate_months'], ['2025-01'])

    def test_missing_month(self):
        del self.cells['A6'], self.cells['B6']
        result = self.check()
        self.assertFalse(result['passed'])
        self.assertEqual(result['missing_months'], ['2025-02'])

    def test_orphan_amount_and_internal_gap(self):
        self.cells['B1000'] = 1
        result = self.check()
        self.assertFalse(result['passed'])
        self.assertEqual(result['invalid_date_rows'], [1000])
        self.assertFalse(result['contiguous_rows'])

    def test_internal_gap_with_complete_month_set(self):
        copy_row(self.cells, MONTH_HEADERS, 6, 7)
        del self.cells['A6'], self.cells['B6']
        self.assertFalse(self.check()['passed'])

    def test_invalid_dates(self):
        for value in (None, '', '45658', True, 45658.5, 45659, 10**15, float('nan'), float('inf')):
            with self.subTest(value=value):
                self.cells['A5'] = value
                self.assertFalse(self.check()['passed'])

    def test_wrong_or_nonfinite_amount(self):
        for value in (-1, None, '100.25', True, float('nan'), float('inf')):
            with self.subTest(value=value):
                self.cells['B5'] = value
                self.assertFalse(self.check()['passed'])

    def test_header_errors(self):
        for column in MONTH_HEADERS:
            with self.subTest(column=column):
                cells = self.cells.copy()
                del cells[column + '4']
                result = check_monthly_output(cells, self.expected)
                self.assertFalse(result['passed'])
                self.assertIn(column, result['header_errors'])

    def test_amount_tolerance(self):
        self.cells['B5'] = 100.254
        self.assertTrue(self.check()['passed'])
        self.cells['B5'] = 100.256
        self.assertFalse(self.check()['passed'])


class SavedPackageTests(unittest.TestCase):
    def setUp(self):
        self.package = dict(cached_errors=[], ref_errors=[], external_link_parts=[],
                            chart_parts=10, pivot_parts=5,
                            sheets=[dict(name=name, state='hidden' if name in HIDDEN_SHEETS else 'visible')
                                    for name in sorted(EXPECTED_SHEETS)])

    def test_designated_structure_passes(self):
        self.assertEqual(package_failures(self.package), [])

    def test_every_error_field_is_mandatory(self):
        for field in ('cached_errors', 'ref_errors', 'external_link_parts'):
            with self.subTest(field=field):
                package = copy.deepcopy(self.package)
                package[field] = ['Deliberate error']
                self.assertTrue(package_failures(package))

    def test_chart_and_pivot_counts_are_mandatory(self):
        for field, values in [('chart_parts', (9, 11)), ('pivot_parts', (4, 6))]:
            for value in values:
                with self.subTest(field=field, value=value):
                    package = copy.deepcopy(self.package)
                    package[field] = value
                    self.assertTrue(package_failures(package))

    def test_missing_extra_or_duplicate_sheet(self):
        for alteration in ('missing', 'extra', 'duplicate'):
            with self.subTest(alteration=alteration):
                package = copy.deepcopy(self.package)
                if alteration == 'missing':
                    package['sheets'].pop()
                elif alteration == 'extra':
                    package['sheets'].append(dict(name='Unexpected', state='visible'))
                else:
                    package['sheets'][0] = package['sheets'][1].copy()
                self.assertIn('Saved worksheet inventory', package_failures(package))

    def test_wrong_sheet_visibility(self):
        for name in ('SalesMonthly', 'DashboardSales'):
            with self.subTest(name=name):
                package = copy.deepcopy(self.package)
                sheet = next(s for s in package['sheets'] if s['name'] == name)
                sheet['state'] = 'visible' if sheet['state'] == 'hidden' else 'hidden'
                self.assertIn('Saved worksheet visibility', package_failures(package))

    def test_required_handoff_identity(self):
        digest = 'a' * 64
        manifest = dict(workbook_path='AdventureWorks-BI.xlsx', workbook_sha256=digest)
        self.assertTrue(handoff_matches(digest, manifest))
        for invalid in (None, {}, {**manifest, 'workbook_path': 'Other.xlsx'},
                        {**manifest, 'workbook_sha256': 'b' * 64}):
            with self.subTest(manifest=invalid):
                self.assertFalse(handoff_matches(digest, invalid))


class CommandLineTests(unittest.TestCase):
    def test_changed_source_fails_before_workbook_open(self):
        # Isolated generated files: this does not touch or download real source data.
        fixture_parent = Path(__file__).resolve().parents[1] / 'data/validation/test-fixtures'
        fixture_parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='awbi-verifier-test-', dir=fixture_parent) as directory:
            root = Path(directory).resolve()
            self.assertTrue(root.is_relative_to(fixture_parent.resolve()))
            raw = root / 'data/raw/adventureworks-oltp-8fe3fd0c'
            raw.mkdir(parents=True)
            evidence = root / 'docs/validation'
            evidence.mkdir(parents=True)
            hashes = []
            for name, width in dict(Customer=7, Product=25, ProductCategory=4,
                                    ProductSubcategory=5, SalesOrderDetail=11,
                                    SalesOrderHeader=26, SalesTerritory=10).items():
                data = ('\t'.join([name] + ['0'] * (width - 1)) + '\n').encode()
                (raw / (name + '.csv')).write_bytes(data)
                hashes.append(hashlib.sha256(data).hexdigest())
            (evidence / '2026-11-06-initial-sales-load.md').write_text('\n'.join(hashes), encoding='utf-8')
            with (raw / 'ProductCategory.csv').open('ab') as stream:
                stream.write(b'Changed\t0\t0\t0\n')
            output = root / 'result.json'
            script = Path(__file__).resolve().parents[1] / 'scripts/verify.py'
            run = subprocess.run([sys.executable, str(script), '--repo', str(root), '--output', str(output)],
                                 capture_output=True, text=True, timeout=30)
            self.assertEqual(run.returncode, 1, run.stderr)
            result = json.loads(output.read_text(encoding='utf-8'))
            self.assertEqual(result['status'], 'FAIL')
            self.assertFalse(result['sources']['ProductCategory']['hash_matches_document'])
            self.assertTrue(all(v['bad_width_rows'] == 0 for v in result['sources'].values()))
            self.assertFalse((root / 'AdventureWorks-BI.xlsx').exists())


if __name__ == '__main__':
    unittest.main()
