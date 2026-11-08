"""Read-only checks of the AWBI pinned sources and saved Excel outputs.

Run with Python 3.12+: python scripts/verify.py --output data/validation/latest.json
No workbook edits, recalculation, refresh, or source downloads are performed.
"""
import argparse
import collections
import csv
import datetime as dt
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
import pathlib
import re
import statistics
import sys
import urllib.parse
import xml.etree.ElementTree as ET
import zipfile

from workbook_checks import check_rfm_output, check_monthly_output, package_failures, handoff_matches

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo', type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
parser.add_argument('--output', type=pathlib.Path, default=pathlib.Path('data/validation/latest.json'))
args = parser.parse_args()
repo = args.repo.resolve()
out = args.output.resolve()
out.parent.mkdir(parents=True, exist_ok=True)
ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
raw = repo / 'data/raw/adventureworks-oltp-8fe3fd0c'
expected_columns = dict(Customer=7, Product=25, ProductCategory=4,
                        ProductSubcategory=5, SalesOrderDetail=11,
                        SalesOrderHeader=26, SalesTerritory=10)
sources = {}
source_info = {}
baseline_text = (repo / 'docs/validation/2026-11-06-initial-sales-load.md').read_text(encoding='utf-8')
for name, width in expected_columns.items():
    path = raw / (name + '.csv')
    data = path.read_bytes()
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.reader(stream, delimiter='\t'))
    sources[name] = rows
    digest = hashlib.sha256(data).hexdigest()
    source_info[name] = {'rows': len(rows), 'sha256': digest,
                         'hash_matches_document': digest in baseline_text,
                         'bad_width_rows': sum(len(r) != width for r in rows)}

if any(not x['hash_matches_document'] or x['bad_width_rows'] for x in source_info.values()):
    out.write_text(json.dumps({'status': 'FAIL', 'sources': source_info, 'reason': 'Inputs do not match the pinned source contract.'}, indent=2), encoding='utf-8')
    sys.exit('FAIL: pinned source hash/schema mismatch; see output JSON.')

headers = {r[0]: r for r in sources['SalesOrderHeader']}
products = {r[0]: r for r in sources['Product']}
subcats = {r[0]: r for r in sources['ProductSubcategory']}
cats = {r[0]: r[1] for r in sources['ProductCategory']}
territories = {r[0]: r[1] for r in sources['SalesTerritory']}
customers = {r[0]: r for r in sources['Customer']}
key_checks = {}
for name, rows in sources.items():
    keys = [(r[0], r[1]) if name == 'SalesOrderDetail' else r[0] for r in rows]
    key_checks[name + '_duplicate_keys'] = len(keys) - len(set(keys))
    key_checks[name + '_empty_keys'] = sum(any(v == '' for v in k) if isinstance(k, tuple) else k == '' for k in keys)
key_checks.update({
    'detail_without_order': sum(r[0] not in headers for r in sources['SalesOrderDetail']),
    'detail_without_product': sum(r[4] not in products for r in sources['SalesOrderDetail']),
    'header_without_customer': sum(r[10] not in customers for r in headers.values()),
    'header_without_territory': sum(r[12] not in territories for r in headers.values()),
    'invalid_product_subcategory': sum(bool(r[18]) and r[18] not in subcats for r in products.values()),
    'subcategory_without_category': sum(r[1] not in cats for r in subcats.values()),
})

entry = {}
annual = {}
months = collections.defaultdict(Decimal)
groups = {}
rfm = {}
line_by_order = collections.defaultdict(Decimal)
sales = Decimal(0)
units = 0
orders = set()
pricing_mismatches = 0
asof = dt.date(2025, 6, 29)
start = dt.date(2022, 5, 30)
for r in sources['SalesOrderDetail']:
    h = headers[r[0]]
    amount = Decimal(r[8])
    qty = int(r[3])
    line_by_order[r[0]] += amount
    pricing_mismatches += amount != Decimal(r[6]) * (1 - Decimal(r[7])) * qty
    if h[5] != '5':
        continue
    date = dt.date.fromisoformat(h[2][:10])
    sales += amount
    units += qty
    orders.add(r[0])
    months[date.strftime('%Y-%m')] += amount
    e = entry.setdefault(h[6], {'sales': Decimal(0), 'units': 0, 'orders': set()})
    e['sales'] += amount; e['units'] += qty; e['orders'].add(r[0])
    a = annual.setdefault(date.year, {'units': 0, 'orders': set()})
    a['units'] += qty; a['orders'].add(r[0])
    product = products[r[4]]
    category = cats[subcats[product[18]][1]] if product[18] else '(blank)'
    key = (territories[h[12]], category)
    g = groups.setdefault(key, {'sales': Decimal(0), 'units': 0, 'orders': set()})
    g['sales'] += amount
    g['units'] += qty
    g['orders'].add(r[0])
    if start <= date <= asof:
        c = rfm.setdefault(int(h[10]), {'date': date, 'orders': set(), 'sales': Decimal(0)})
        c['date'] = max(c['date'], date)
        c['orders'].add(r[0])
        c['sales'] += amount

segments = collections.Counter()
for customer, c in rfm.items():
    c['recency'] = (asof - c['date']).days
    c['frequency'] = len(c.pop('orders'))
    R = 5 - sum(c['recency'] >= x for x in (72, 130, 205, 289))
    F = min(c['frequency'], 5)
    rounded = c['sales'].quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    M = 1 + sum(rounded > Decimal(x) for x in ('39.98', '98.96', '1236.78', '3578.27'))
    segment = ('Champions' if R >= 4 and F >= 3 and M >= 4 else
               'Frequent' if F >= 3 and R >= 3 else 'Recent' if R >= 4 else
               'Less recent repeat' if R <= 2 and F >= 2 else 'Other')
    c.update(R=R, F=F, M=M, segment=segment)
    segments[segment] += 1

cohorts = {}
for customer_id, c in rfm.items():
    master = customers[str(customer_id)]
    kind = 'store' if master[2] else 'person' if master[1] else 'unclassified'
    cohorts.setdefault(kind, []).append(c)
business_review = {
    'order_entry': {flag: {'meaning': 'Customer placed online' if flag == '1' else 'Salesperson placed' if flag == '0' else 'Unknown', 'orders': len(g['orders']), 'units': g['units'], 'source_amount': str(g['sales'])} for flag, g in sorted(entry.items())},
    'annual_volume': {str(year): {'orders': len(g['orders']), 'units': g['units']} for year,g in sorted(annual.items())},
    'customer_cohorts': {kind: {'customers': len(rows), 'repeat_customers': sum(c['frequency'] >= 2 for c in rows), 'repeat_rate': sum(c['frequency'] >= 2 for c in rows)/len(rows), 'median_orders': statistics.median(c['frequency'] for c in rows), 'median_recency': statistics.median(c['recency'] for c in rows), 'segments': dict(collections.Counter(c['segment'] for c in rows))} for kind,rows in sorted(cohorts.items())},
    'population_policy': 'StoreID populated takes precedence; otherwise PersonID populated; otherwise unclassified. CustomerID is the counting grain. Shared RFM bands are descriptive sample bands, not equivalent customer value.',
}

book = repo / 'AdventureWorks-BI.xlsx'
z = zipfile.ZipFile(book)
strings = [''.join(si.itertext()) for si in ET.fromstring(z.read('xl/sharedStrings.xml'))]
wb = ET.fromstring(z.read('xl/workbook.xml'))
rels = {r.attrib['Id']: r.attrib['Target'] for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
sheets = {}
errors = []
ref_errors = []
formula_count = 0
needed = {'CustomerRFM', 'SalesMonthly', 'Validation', 'DashboardSales', 'DashboardCustomers', 'SalesScenario'}
sheet_inventory = []
for sheet in wb.find('m:sheets', ns):
    name = sheet.get('name')
    target = rels[sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
    path = target.lstrip('/') if target.startswith('/') else 'xl/' + target
    sheet_inventory.append({'name': name, 'state': sheet.get('state', 'visible')})
    values = {}
    for _, cell in ET.iterparse(z.open(path), events=('end',)):
        if cell.tag == '{' + ns['m'] + '}row':
            cell.clear()
            continue
        if cell.tag != '{' + ns['m'] + '}c':
            continue
        v = cell.find('m:v', ns)
        f = cell.find('m:f', ns)
        value = v.text if v is not None else None
        if cell.get('t') == 'e':
            errors.append([name, cell.get('r'), value])
        if f is not None:
            formula_count += 1
            if '#REF!' in (f.text or ''):
                ref_errors.append([name, cell.get('r'), f.text])
        if name in needed:
            if cell.get('t') == 's':
                value = strings[int(value)]
            elif cell.get('t') == 'inlineStr':
                value = ''.join(cell.find('m:is', ns).itertext())
            elif value is not None and cell.get('t') not in ('e', 'str'):
                value = float(value)
            if value is not None:
                values[cell.get('r')] = value
        cell.clear()
    if name in needed:
        sheets[name] = values

customer_check = check_rfm_output(sheets['CustomerRFM'], rfm)
monthly_check = check_monthly_output(sheets['SalesMonthly'], months)

group_mismatches = []
max_group_delta = 0.0
v = sheets['Validation']
for row in range(41, 51):
    territory = v['A' + str(row)]
    for idx, col in enumerate('BCDE'):
        category = v[col + '40']
        expected = groups[(territory, category)]
        for column, wanted, tol in [
            (col, float(expected['sales']), .005),
            ('FGHI'[idx], expected['units'], 0),
            ('JKLM'[idx], len(expected['orders']), 0),
            ('NOPQ'[idx], float(expected['sales'] / len(expected['orders'])), .005),
        ]:
            delta = abs(v[column + str(row)] - wanted)
            max_group_delta = max(max_group_delta, delta)
            if (delta >= tol if tol else delta != 0):
                group_mismatches.append([territory, category, column, delta])

md_files = [repo / n for n in ['README.md', 'REPO_CONTEXT.md', 'AGENTS.md', 'THIRD_PARTY_NOTICES.md']]
md_files += sorted((repo / 'docs').rglob('*.md'))
broken_links = []
broken_anchors = []
paragraphs = collections.defaultdict(list)
for file in md_files:
    text = file.read_text(encoding='utf-8')
    for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', text):
        dest = match.group(1).split(' "')[0]
        if '://' in dest or dest.startswith('mailto:'):
            continue
        path, _, anchor = urllib.parse.unquote(dest).partition('#')
        target = (file.parent / path).resolve() if path else file.resolve()
        line = text[:match.start()].count('\n') + 1
        if not target.exists():
            broken_links.append([str(file.relative_to(repo)), line, dest])
        elif anchor and target.suffix == '.md':
            headings = re.findall(r'^#{1,6}\s+(.+)$', target.read_text(encoding='utf-8'), re.M)
            slugs = [re.sub(r'[^\w\s-]', '', h.lower()).replace(' ', '-') for h in headings]
            if anchor not in slugs:
                broken_anchors.append([str(file.relative_to(repo)), line, dest])
    if file.parent == repo / 'docs' or file.name in ('README.md', 'REPO_CONTEXT.md'):
        for para in text.split('\n\n'):
            normalized = ' '.join(para.split())
            if len(normalized) > 150 and not normalized.startswith(('|', '```')):
                paragraphs[normalized].append(str(file.relative_to(repo)))

result = {
    'verifier_version': 2,
    'baseline': {'source_revision': '8fe3fd0c9a825fef3ae6d601e97537b612d7b214',
                 'sha256': hashlib.sha256(book.read_bytes()).hexdigest(), 'workbook_bytes': book.stat().st_size},
    'sources': source_info,
    'business_review': business_review,
    'source_key_violations': key_checks,
    'independent_source': {
        'shipped_sales': str(sales), 'units': units, 'orders': len(orders),
        'aov': str(sales / len(orders)), 'months': len(months), 'customers': len(rfm),
        'segments': dict(segments), 'median_recency': statistics.median(c['recency'] for c in rfm.values()),
        'median_orders': statistics.median(c['frequency'] for c in rfm.values()),
        'median_sales': str(statistics.median(c['sales'] for c in rfm.values())),
        'pricing_mismatches_exact_decimal': pricing_mismatches,
        'header_subtotals_not_matching_four_decimal_half_up': sum(
            Decimal(h[19]) != line_by_order[k].quantize(Decimal('.0001'), rounding=ROUND_HALF_UP)
            for k, h in headers.items()),
        'header_order_flags': dict(collections.Counter(h[6] for h in headers.values())),
        'customer_person_store_mix': dict(collections.Counter(
            'store' if customers[str(c)][2] else 'person' if customers[str(c)][1] else 'other' for c in rfm)),
    },
    'saved_output_comparison': {
        'customers': customer_check,
        'monthly': monthly_check,
        'territory_category_groups_compared': 40, 'group_mismatches': group_mismatches,
        'max_group_delta': max_group_delta,
        'sales_dashboard_values': {k: sheets['DashboardSales'][k] for k in ['B9', 'L9', 'V9', 'AF9']},
        'customer_dashboard_values': {k: sheets['DashboardCustomers'][k] for k in ['B9', 'L9', 'V9', 'AF9']},
    },
    'saved_package': {'sheets': sheet_inventory, 'formula_elements': formula_count,
                      'cached_errors': errors, 'ref_errors': ref_errors,
                      'external_link_parts': [n for n in z.namelist() if n.startswith('xl/externalLinks/')],
                      'chart_parts': len([n for n in z.namelist() if re.fullmatch(r'xl/charts/chart\d+\.xml', n)]),
                      'pivot_parts': len([n for n in z.namelist() if re.fullmatch(r'xl/pivotTables/pivotTable\d+\.xml', n)])},
    'documentation': {'markdown_files_scanned': len(md_files), 'broken_links': broken_links,
                       'anchor_candidates_to_review': broken_anchors,
                       'exact_long_paragraph_duplicates': [{'text': k, 'files': v} for k, v in paragraphs.items() if len(v) > 1]},
    'limits': ['Saved cached outputs only: no new interactive-filter test, refresh, save or DAX formula readback.',
               'Arithmetic reconciliation does not establish currency comparability or business causality.',
               'The same assistant ran source calculations and workbook inspection; this is not independent human review.'],
}
failures = []
def require(condition, label):
    if not condition:
        failures.append(label)
require(not any(key_checks.values()), 'Source keys or references')
require(pricing_mismatches == 0, 'Source pricing identity')
require(result['independent_source']['header_subtotals_not_matching_four_decimal_half_up'] == 0, 'Header subtotal rounding')
failures.extend(package_failures(result['saved_package']))
require(customer_check['passed'], 'Complete customer output population/headers/values')
require(monthly_check['passed'], 'Complete monthly output population/headers/values')
require(not group_mismatches, 'Territory/category groups')
require(not broken_links and not broken_anchors, 'Documentation links/anchors')
require(sheets['DashboardSales']['L9'] == units and sheets['DashboardSales']['V9'] == len(orders), 'Sales count cards')
require(abs(sheets['DashboardSales']['B9'] - float(sales)) < .005, 'Sales amount card')
require(abs(sheets['DashboardSales']['AF9'] - float(sales / len(orders))) < .005, 'AOV card')
require(sheets['DashboardCustomers']['B9'] == len(rfm), 'Customer count card')
require(sheets['DashboardCustomers']['L9'] == result['independent_source']['median_recency'], 'Recency median card')
require(sheets['DashboardCustomers']['V9'] == result['independent_source']['median_orders'], 'Orders median card')
require(abs(sheets['DashboardCustomers']['AF9'] - float(result['independent_source']['median_sales'])) < .005, 'Customer sales median card')
require(sheets['SalesScenario']['B7'] == 0 and sheets['SalesScenario']['B8'] == 0, 'Scenario defaults')
require(abs(sheets['SalesScenario']['B5'] - float(sales)) < .005 and abs(sheets['SalesScenario']['B10'] - float(sales)) < .005, 'Scenario baseline/default result')
manifest = repo / 'docs/handoff.json'
handoff = json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else None
require(handoff_matches(result['baseline']['sha256'], handoff), 'Required designated handoff identity')
result['status'] = 'FAIL' if failures else 'PASS'
result['failed_checks'] = failures
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'failed_checks': failures, 'business_review': business_review, 'output': str(args.output)}, indent=2))
sys.exit(1 if failures else 0)
