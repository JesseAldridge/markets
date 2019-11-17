import _0_parse_oecd

sector_info = _0_parse_oecd.SectorInfo()
sector_by_country_by_year_to_gdp_percent = sector_info.sector_by_country_by_year_to_gdp_percent

for year in range(2000, 2018):
  sum_ = 0
  sum_no_services_lower = 0
  sum_no_services = 0
  sum_no_services_no_manufacturing = 0
  for sector in sector_by_country_by_year_to_gdp_percent:
    value = sector_by_country_by_year_to_gdp_percent[sector]['CHN'][year]
    # print(round(value, 2), sector)
    sum_ += value
    if 'services' not in sector.lower():
      sum_no_services_lower += value
    if sector != 'Services':
      sum_no_services += value
    if sector != 'Services' and sector != 'Manufacturing':
      sum_no_services_no_manufacturing += value

  # print()
  # print('total no services lower:', round(sum_no_services_lower, 2))
  # print('total no Services:', round(sum_no_services, 2))
  print('total no Services no Manufacturing:', round(sum_no_services_no_manufacturing, 2))
  # print('total:', round(sum_, 2))

