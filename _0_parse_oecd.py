import csv, io

def read_oecp_csv(name, ignore=None):
  if ignore is None:
    ignore = {}

  with io.open('{}.csv'.format(name), 'r', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

  subject_to_english = {
    'AGRFORTFISH': 'Agriculture, forestry, fishing',
    'CONSTR': 'Construction',
    'ENRG': 'Energy',
    'FINANCEINS': 'Finance and insurance',
    'FOOD': 'Food',
    'INDUSENRG': 'Industry, including energy',
    'INFCOMM': 'Information, communication',
    'MFG': 'Manufacturing',
    'OTHSERVACT': 'Other services activities',
    'PROSCISUPP': 'Professional, scientific, support services',
    'PUBADMINEDUSOC': 'Public administration, defence, education, health, social work',
    'REALEST': 'Real estate',
    'SERV': 'Services',
    'TOT': 'Total',
    'TOT_FOODENRG': 'Total Food Energy',
    'WHLEHTELTRANSP': 'Wholesale, retail trade, repairs, transport; accommodation, food services',
  }

  for row in rows:
    for key in ignore:
      if row[key] in ignore[key]:
        break
    else:
      yield (
        row['LOCATION'],
        int(row['TIME']),
        float(row['Value']),
        subject_to_english[row['SUBJECT']],
        row['MEASURE'],
        row['FREQUENCY'],
      )

def read_gdp_data(path):
  return read_oecp_csv(path, ignore={
    'LOCATION': ('EA', 'EA19', 'EU', 'OECDE', 'OECD'),
    'MEASURE': ('AGRWTH', 'USD_CAP'),
  })

class GDPTotalInfo:
  # https://data.oecd.org/gdp/gross-domestic-product-gdp.htm

  def __init__(self):
    self.country_by_year_to_gdp_total = {}
    self.countries = set()
    self.min_year, self.max_year = None, None
    for country, year, gdp, _, _, _ in read_gdp_data('data/gdp-total'):
      self.countries.add(country)
      if self.min_year is None or year < self.min_year:
        self.min_year = year
      if self.max_year is None or year > self.max_year:
        self.max_year = year

      self.country_by_year_to_gdp_total.setdefault(country, {})
      self.country_by_year_to_gdp_total[country].setdefault(year, {})
      self.country_by_year_to_gdp_total[country][year] = gdp

    # fill in missing values with previous value or zero if there is not previous value
    for country in self.country_by_year_to_gdp_total:
      year_to_gdp = self.country_by_year_to_gdp_total[country]
      self.fill_in_missing_years(year_to_gdp)

  def fill_in_missing_years(self, year_to_gdp):
    prev_year_val = None
    for year in range(self.min_year, self.max_year + 1):
      if year not in year_to_gdp:
        year_to_gdp[year] = prev_year_val if prev_year_val is not None else 0
      prev_year_val = year_to_gdp[year]

class SectorInfo(GDPTotalInfo):
  # https://data.oecd.org/natincome/value-added-by-activity.htm

  def __init__(self):
    super().__init__()
    self.sector_by_country_by_year_to_gdp = {}
    for country, year, percent_gdp, sector, _, _ in read_gdp_data('data/gdp-by-industry'):
      gdp_total = self.country_by_year_to_gdp_total[country][year]
      gdp_sector = (percent_gdp / 100) * gdp_total
      self.add_row(country, year, percent_gdp, sector, gdp_sector)

    # fill in missing values with previous value or zero if there is not previous value
    for sector in self.sector_by_country_by_year_to_gdp:
      for country in self.countries:
        country_by_year_to_gdp = self.sector_by_country_by_year_to_gdp[sector]
        country_by_year_to_gdp.setdefault(country, {})
        self.fill_in_missing_years(country_by_year_to_gdp[country])

  def add_row(self, country, year, percent_gdp, sector, gdp):
    self.sector_by_country_by_year_to_gdp.setdefault(sector, {})
    self.sector_by_country_by_year_to_gdp[sector].setdefault(country, {})
    self.sector_by_country_by_year_to_gdp[sector][country].setdefault(year, 0)
    self.sector_by_country_by_year_to_gdp[sector][country][year] += gdp

def get_year_to_cpi():
  year_to_cpi = {}
  ignore={
    'FREQUENCY': ('Q', 'M'),
  }
  for location, year, value, subject, measure, frequency in read_oecp_csv('data/cpi', ignore):
    if location == 'OECD' and subject == 'Total' and measure == 'IDX2015' and frequency == 'A':
      year_to_cpi[year] = value
  return year_to_cpi
