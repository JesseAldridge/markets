import _0_parse_oecd

sector_info = _0_parse_oecd.SectorInfo()
sector_by_country_by_year_to_gdp_percent = sector_info.sector_by_country_by_year_to_gdp_percent

for year in range(2000, 2018):
  for country in sector_info.countries:
    sum_ = 0
    for sector in sector_by_country_by_year_to_gdp_percent:
      value = sector_by_country_by_year_to_gdp_percent[sector][country][year]
      if sector != 'Services' and sector != 'Manufacturing':
        sum_ += value

    print('total gdp percent:', round(sum_, 2))
    assert round(sum_) in (100, 0)
print('looks good')
