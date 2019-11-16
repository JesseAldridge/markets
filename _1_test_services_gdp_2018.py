import _0_parse_oecd

sector_by_country_by_year_to_gdp = _0_parse_oecd.SectorInfo().sector_by_country_by_year_to_gdp
sector = 'Services'

def services_gdp(year):
  gdp_services = 0
  for country in sector_by_country_by_year_to_gdp[sector]:
    year_to_gdp = sector_by_country_by_year_to_gdp[sector][country]
    gdp_services += year_to_gdp[year] * 10 ** 6
  print('GDP {}: ${:,}'.format(year, int(gdp_services)))
  return gdp_services

assert services_gdp(2016) < services_gdp(2017) < services_gdp(2018)
