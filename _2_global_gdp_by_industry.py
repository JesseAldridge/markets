import _0_parse_oecd

# Global GDP by sector
sector_by_year_to_gdp = _0_parse_oecd.get_sector_by_year_to_gdp()
with open('out.csv', 'w') as f:
  years = sector_by_year_to_gdp[sector_by_year_to_gdp.keys()[0]].keys()
  f.write(','.join(['sector'] + [str(year) for year in years]) + '\n')
  for sector in sector_by_year_to_gdp:
    val_strs = []
    for year in sector_by_year_to_gdp[sector]:
      val_strs.append(str(sector_by_year_to_gdp[sector][year]))
    f.write('"{}",{}\n'.format(sector, ','.join(val_strs)))

# Global GDP by country, energy sector
sector_by_year_by_country_to_gdp = _0_parse_oecd.get_sector_by_year_by_country_to_gdp()
country_to_gdp = sector_by_year_by_country_to_gdp['Industry, including energy'][2018]
energy_gdp = sum(country_to_gdp.values())
for country in sorted(country_to_gdp, key=lambda country: -country_to_gdp[country]):
  print country, round(country_to_gdp[country] / energy_gdp, 2)
