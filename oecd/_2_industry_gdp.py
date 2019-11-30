import _0_parse_oecd

sector_info = _0_parse_oecd.SectorInfo()
sector_by_country_by_year_to_gdp = sector_info.sector_by_country_by_year_to_gdp

def sector_size(sector):
  sum_of_sums = 0
  for country in sector_by_country_by_year_to_gdp[sector]:
    sum_of_sums += sum(sector_by_country_by_year_to_gdp[sector][country].values())
  return sum_of_sums

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
  country_by_year_to_gdp = sector_by_country_by_year_to_gdp[sector]

  def gdp_2018(country):
    return country_by_year_to_gdp[country][2018]

  sum_industry_gdp = 0
  for country in country_by_year_to_gdp:
    sum_industry_gdp += gdp_2018(country)

  print('sector:', sector)
  for country in sorted(country_by_year_to_gdp, key=gdp_2018, reverse=True)[:5]:
    country_percent_of_sector = country_by_year_to_gdp[country][2018] / sum_industry_gdp

    print(country, round(country_percent_of_sector, 2))

def gdp_total_2018(country):
  return sector_info.country_by_year_to_gdp_total[country][2018]

print()
print('GDP by country:')
for country in sorted(sector_info.countries, key=gdp_total_2018, reverse=True)[:5]:
  print('{}, {:,}'.format(country, gdp_total_2018(country)))
