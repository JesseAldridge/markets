import _0_parse_oecd

# Global GDP by sector
sector_info = _0_parse_oecd.SectorInfo()
sector_by_year_by_country_to_gdp = sector_info.sector_by_year_by_country_to_gdp
with open('out.csv', 'w') as f:
  years = range(sector_info.min_year, sector_info.max_year)
  f.write(','.join(['sector'] + [str(year) for year in years]) + '\n')
  for sector in sector_by_year_by_country_to_gdp:
    val_strs = []
    for year in sector_by_year_by_country_to_gdp[sector]:
      val_strs.append(str(sum(sector_by_year_by_country_to_gdp[sector][year].values())))
    f.write('"{}",{}\n'.format(sector, ','.join(val_strs)))
