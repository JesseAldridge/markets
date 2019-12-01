import _0_parse_oecd

sector_info = _0_parse_oecd.SectorInfo()
sector_by_country_by_year_to_gdp_percent = sector_info.sector_by_country_by_year_to_gdp_percent

def sector_size(sector):
  sum_of_sums = 0
  for country in sector_by_country_by_year_to_gdp_percent[sector]:
    sum_of_sums += sum(sector_by_country_by_year_to_gdp_percent[sector][country].values())
  return sum_of_sums

sum_ = 0
for sector in sorted((
  'Agriculture, forestry, fishing',
  'Construction',
  'Finance and insurance',
  'Industry, including energy',
  'Information, communication',
  'Other services activities',
  'Professional, scientific, support services',
  'Public administration, defence, education, health, social work',
  'Real estate',
  'Wholesale, retail trade, repairs, transport; accommodation, food services',
), key=sector_size, reverse=True):
  gdp_percent = round(sector_by_country_by_year_to_gdp_percent[sector]['USA'][2018], 2)
  print('sector:', gdp_percent, sector)
  sum_ += gdp_percent
print('sum:', sum_)


import _0_parse_oecd

# Global GDP by sector
sector_info = _0_parse_oecd.SectorInfo()
sector_by_country_by_year_to_gdp = sector_info.sector_by_country_by_year_to_gdp
years = range(1980, sector_info.max_year + 1)

year_to_cpi = _0_parse_oecd.get_year_to_cpi()
with open('gdp-per-sector-USA-infl-adjusted.csv', 'w') as f:
  f.write(','.join(['sector'] + [str(year) for year in years]) + '\n')
  for sector in sector_by_country_by_year_to_gdp:
    val_strs = []
    for year in years:
      gdp = sector_by_country_by_year_to_gdp[sector]['USA'][year]
      cpi = year_to_cpi[year]
      val_strs.append(str(gdp / (cpi / 100)))
    f.write('"{}",{}\n'.format(sector, ','.join(val_strs)))
