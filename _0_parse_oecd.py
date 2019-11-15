import csv, io

def read_oecp_csv(name):
  with io.open('{}.csv'.format(name), 'r', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

  subject_to_english = {
    'TOT': 'Total',
    'AGRFORTFISH': 'Agriculture, forestry, fishing',
    'INDUSENRG': 'Industry, including energy',
    'MFG': 'Manufacturing',
    'CONSTR': 'Construction',
    'WHLEHTELTRANSP': 'Wholesale, retail trade, repairs, transport; accommodation, food services',
    'INFCOMM': 'Information, communication',
    'FINANCEINS': 'Finance and insurance',
    'REALEST': 'Real estate',
    'PROSCISUPP': 'Professional, scientific, support services',
    'PUBADMINEDUSOC': 'Public administration, defence, education, health, social work',
    'OTHSERVACT': 'Other services activities',
    'SERV': 'Services',
  }

  for row in rows:
    if row['LOCATION'] in ('EA', 'EA19', 'EU', 'OECDE', 'OECD'):
      continue
    if row['MEASURE'] in ('AGRWTH', 'USD_CAP'):
      continue
    yield (
      row['LOCATION'],
      int(row['TIME']),
      float(row['Value']),
      subject_to_english[row['SUBJECT']],
    )

def get_country_by_year_to_gdp():
  country_by_year_to_gdp = {}
  # https://data.oecd.org/gdp/gross-domestic-product-gdp.htm
  for country, year, gdp, _ in read_oecp_csv('gdp-total'):
    country_by_year_to_gdp.setdefault(country, {})
    country_by_year_to_gdp[country].setdefault(year, {})
    country_by_year_to_gdp[country][year] = gdp
  return country_by_year_to_gdp

def get_sector_by_year_to_gdp():
  country_by_year_to_gdp = get_country_by_year_to_gdp()
  sector_by_year_to_gdp = {}
  min_year, max_year = None, None
  # https://data.oecd.org/natincome/value-added-by-activity.htm
  for country, year, percent_gdp, sector in read_oecp_csv('gdp-by-industry'):
    gdp = (percent_gdp / 100) * country_by_year_to_gdp[country].get(year, 0)

    sector_by_year_to_gdp.setdefault(sector, {})
    sector_by_year_to_gdp[sector].setdefault(year, 0)
    sector_by_year_to_gdp[sector][year] += gdp
    if min_year is None or year < min_year:
      min_year = year
    if max_year is None or year > max_year:
      max_year = year

  return sector_by_year_to_gdp

def get_sector_by_year_by_country_to_gdp():
  country_by_year_to_gdp = get_country_by_year_to_gdp()
  sector_by_year_by_country_to_gdp = {}
  min_year, max_year = None, None
  # https://data.oecd.org/natincome/value-added-by-activity.htm
  for country, year, percent_gdp, sector in read_oecp_csv('gdp-by-industry'):
    gdp = (percent_gdp / 100) * country_by_year_to_gdp[country].get(year, 0)

    sector_by_year_by_country_to_gdp.setdefault(sector, {})
    sector_by_year_by_country_to_gdp[sector].setdefault(year, {})
    sector_by_year_by_country_to_gdp[sector][year].setdefault(country, 0)
    sector_by_year_by_country_to_gdp[sector][year][country] += gdp
    if min_year is None or year < min_year:
      min_year = year
    if max_year is None or year > max_year:
      max_year = year

  return sector_by_year_by_country_to_gdp
