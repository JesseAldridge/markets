import _0_parse_oecd

# Global GDP by sector
sector_info = _0_parse_oecd.SectorInfo()
sector_by_country_by_year_to_gdp = sector_info.sector_by_country_by_year_to_gdp
years = range(1980, sector_info.max_year + 1)
countries = sector_info.countries

year_to_cpi = _0_parse_oecd.get_year_to_cpi()
with open('gdp-per-sector-infl-adjusted.csv', 'w') as f:
  f.write(','.join(['sector'] + [str(year) for year in years]) + '\n')
  for sector in sector_by_country_by_year_to_gdp:
    country_by_year_to_gdp = sector_by_country_by_year_to_gdp[sector]
    val_strs = []
    for year in years:
      for country in country_by_year_to_gdp:
        if year not in country_by_year_to_gdp[country]:
          print('missing row:', sector, country, year)
      gdp = sum(country_by_year_to_gdp[country][year] for country in country_by_year_to_gdp)
      cpi = year_to_cpi[year]
      val_strs.append(str(gdp / (cpi / 100)))
    f.write('"{}",{}\n'.format(sector, ','.join(val_strs)))
