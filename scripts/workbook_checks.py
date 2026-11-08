"""Saved-output contracts used by the verifier and its synthetic regression tests."""
import collections
import datetime as dt
import math
import re


EPOCH = dt.date(1899, 12, 30)
RFM_HEADERS = dict(zip('ABCDEFGHI', (
    'Row Labels', 'RFM Last Order', 'RFM Recency Days', 'RFM Orders',
    'RFM Sales', 'RFM R Score', 'RFM F Score', 'RFM M Score', 'RFM Segment',
)))
MONTH_HEADERS = {'A': 'Order month', 'B': 'Shipped sales'}
EXPECTED_SHEETS = {
    'DashboardSales', 'DashboardCustomers', 'SalesScenario', 'SalesOverview',
    'SalesMonthly', 'CustomerOverview', 'SalesByDate', 'CustomerRFM', 'RFMGuide',
    'Validation', 'KeyChecks', 'DashboardData', 'SourceConfig', 'SalesOrderHeader',
    'SalesOrderDetail', 'Product', 'ProductSubcategory', 'ProductCategory',
    'Customer', 'SalesTerritory',
}
HIDDEN_SHEETS = {'SalesOverview', 'SalesMonthly', 'CustomerOverview'}


def numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def output_rows(values, columns, first_row):
    """Enumerate populated output cells, including rows after an intervening gap.

    This examines the saved cells already read from XML, not Excel's empty grid.
    """
    rows = {}
    for address, value in values.items():
        match = re.fullmatch(r'([A-Z]+)([1-9][0-9]*)', address)
        if not match or value is None or value == '':
            continue
        column, row = match[1], int(match[2])
        if column in columns and row >= first_row:
            rows.setdefault(row, {})[column] = value
    return dict(sorted(rows.items()))


def check_headers(values, expected, row):
    return {col: {'expected': label, 'actual': values.get(f'{col}{row}')}
            for col, label in expected.items() if values.get(f'{col}{row}') != label}


def check_rfm_output(values, expected):
    rows = output_rows(values, RFM_HEADERS, 6)
    seen, mismatches, invalid_rows = [], [], []
    max_delta = 0.0
    for row, cells in rows.items():
        customer = cells.get('A')
        if not numeric(customer) or customer <= 0 or not float(customer).is_integer():
            invalid_rows.append(row)
            continue
        customer = int(customer)
        seen.append(customer)
        if customer not in expected:
            continue
        source = expected[customer]
        wanted = {'B': (source['date'] - EPOCH).days, 'C': source['recency'],
                  'D': source['frequency'], 'E': float(source['sales']),
                  'F': source['R'], 'G': source['F'], 'H': source['M'], 'I': source['segment']}
        for col, value in wanted.items():
            actual = cells.get(col)
            if col == 'I':
                same = actual == value
            elif numeric(actual):
                delta = abs(actual - value)
                if col == 'E':
                    max_delta = max(max_delta, delta)
                same = delta < .005 if col == 'E' else delta == 0
            else:
                same = False
            if not same:
                mismatches.append({'row': row, 'customer': customer, 'column': col,
                                   'expected': value, 'actual': actual})
    counts = collections.Counter(seen)
    result = {
        'rows_compared': len(rows), 'headers': {col: values.get(col + '5') for col in RFM_HEADERS},
        'header_errors': check_headers(values, RFM_HEADERS, 5), 'invalid_id_rows': invalid_rows,
        'missing_customers': sorted(set(expected) - set(seen)),
        'unexpected_customers': sorted(set(seen) - set(expected)),
        'duplicate_customers': sorted(k for k, count in counts.items() if count > 1),
        'contiguous_rows': list(rows) == list(range(6, 6 + len(rows))),
        'mismatches': mismatches, 'max_sales_delta': max_delta,
    }
    result['passed'] = (not any(result[k] for k in (
        'header_errors', 'invalid_id_rows', 'missing_customers', 'unexpected_customers',
        'duplicate_customers', 'mismatches')) and result['contiguous_rows'])
    return result


def check_monthly_output(values, expected):
    rows = output_rows(values, MONTH_HEADERS, 5)
    seen, mismatches, invalid_rows = [], [], []
    max_delta = 0.0
    for row, cells in rows.items():
        serial = cells.get('A')
        if not numeric(serial) or not float(serial).is_integer():
            invalid_rows.append(row)
            continue
        try:
            date = EPOCH + dt.timedelta(days=int(serial))
        except (OverflowError, ValueError):
            invalid_rows.append(row)
            continue
        if date.day != 1:
            invalid_rows.append(row)
        key = date.strftime('%Y-%m')
        seen.append(key)
        if key not in expected:
            continue
        actual, wanted = cells.get('B'), float(expected[key])
        if numeric(actual):
            delta = abs(actual - wanted)
            max_delta = max(max_delta, delta)
            same = delta < .005
        else:
            same = False
        if not same:
            mismatches.append({'row': row, 'month': key, 'expected': wanted, 'actual': actual})
    counts = collections.Counter(seen)
    result = {
        'rows_compared': len(rows), 'header_errors': check_headers(values, MONTH_HEADERS, 4),
        'invalid_date_rows': invalid_rows, 'missing_months': sorted(set(expected) - set(seen)),
        'unexpected_months': sorted(set(seen) - set(expected)),
        'duplicate_months': sorted(k for k, count in counts.items() if count > 1),
        'contiguous_rows': list(rows) == list(range(5, 5 + len(rows))),
        'mismatches': mismatches, 'max_sales_delta': max_delta,
    }
    result['passed'] = (not any(result[k] for k in (
        'header_errors', 'invalid_date_rows', 'missing_months', 'unexpected_months',
        'duplicate_months', 'mismatches')) and result['contiguous_rows'])
    return result


def package_failures(package):
    """Enforce the designated artifact's saved-package structure, not general Excel support."""
    failures = []
    for field, label in [('cached_errors', 'Saved cell errors'), ('ref_errors', 'Broken worksheet references'),
                         ('external_link_parts', 'External workbook links')]:
        if package[field]:
            failures.append(label)
    for field, expected in [('chart_parts', 10), ('pivot_parts', 5)]:
        if package[field] != expected:
            failures.append(f'Saved {field} count (expected {expected})')
    inventory = package['sheets']
    if len(inventory) != len(EXPECTED_SHEETS) or {s['name'] for s in inventory} != EXPECTED_SHEETS:
        failures.append('Saved worksheet inventory')
    if any(s['state'] != ('hidden' if s['name'] in HIDDEN_SHEETS else 'visible') for s in inventory):
        failures.append('Saved worksheet visibility')
    return failures


def handoff_matches(actual_hash, manifest):
    return (isinstance(manifest, dict)
            and manifest.get('workbook_path') == 'AdventureWorks-BI.xlsx'
            and manifest.get('workbook_sha256') == actual_hash)
