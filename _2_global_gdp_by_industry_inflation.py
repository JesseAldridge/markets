import _0_parse_oecd

# Global GDP by sector
sector_info = _0_parse_oecd.get_sector_by_year_by_country_to_gdp()
sector_by_year_by_country_to_gdp = sector_info.sector_by_year_by_country_to_gdp
years = range(sector_info.min_year, sector_info.max_year)
countries = sector_info.countries

year_to_cpi = _0_parse_oecd.get_year_to_cpi()
with open('gdp-per-sector-infl-adjusted.csv', 'w') as f:
  f.write(','.join(['sector'] + [str(year) for year in years]) + '\n')
  for sector in sector_by_year_by_country_to_gdp:
    val_strs = []
    year_by_country_to_gdp = sector_by_year_by_country_to_gdp[sector]
    for year in year_to_cpi:
      cpi = year_to_cpi[year]
      val_strs.append(str(sum(year_by_country_to_gdp[year].values()) / (cpi / 100)))
    f.write('"{}",{}\n'.format(sector, ','.join(val_strs)))
