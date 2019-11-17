import _0_parse_oecd

sector_info = _0_parse_oecd.SectorInfo()
sector_by_country_by_year_to_gdp_percent = sector_info.sector_by_country_by_year_to_gdp_percent

for year in range(2000, 2018):
  for country in sector_info.countries:
    sum_ = 0
    sum_no_services_lower = 0
    sum_no_services = 0
    sum_no_services_no_manufacturing = 0
    for sector in sector_by_country_by_year_to_gdp_percent:
      value = sector_by_country_by_year_to_gdp_percent[sector][country][year]
      sum_ += value
      if 'services' not in sector.lower():
        sum_no_services_lower += value
      if sector != 'Services':
        sum_no_services += value
      if sector != 'Services' and sector != 'Manufacturing':
        sum_no_services_no_manufacturing += value

    print('total no Services no Manufacturing:', round(sum_no_services_no_manufacturing, 2))
    assert round(sum_no_services_no_manufacturing) in (100, 0)
print 'looks good'
