import _0_parse_oecd

sector_by_country_by_year_to_gdp = _0_parse_oecd.SectorInfo().sector_by_country_by_year_to_gdp
sector = 'Agriculture, forestry, fishing'

def agg_gdp(year):
  gdp_services = 0
  for country in sector_by_country_by_year_to_gdp[sector]:
    year_to_gdp = sector_by_country_by_year_to_gdp[sector][country]
    gdp_services += year_to_gdp[year] * 10 ** 6
  print('GDP {}: ${:,}'.format(year, int(gdp_services)))
  return gdp_services

assert agg_gdp(2016) < agg_gdp(2017) < agg_gdp(2018)
