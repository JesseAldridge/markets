import _0_parse_oecd

sector_by_country_by_year_to_gdp = _0_parse_oecd.SectorInfo().sector_by_country_by_year_to_gdp
country_by_year_to_gdp = sector_by_country_by_year_to_gdp['Agriculture, forestry, fishing']
gdp_agr_1980 = 0
for country in country_by_year_to_gdp:
  gdp_agr_1980 += country_by_year_to_gdp[country][1980] * 10 ** 6

print('my_result: ${:,}'.format(int(gdp_agr_1980)))


# --- OECD Manual calculation ---

# https://data.oecd.org/natincome/value-added-by-activity.htm

country_to_percent_gdp_agr_1980 = {
  'China': 29.9,
  'Korea': 15.9,
  'New Zealand': 11.1,
  'Finland': 9.6,
  'Sweden': 5.3,
  'Austria': 4.9,
  'Denmark': 4.7,
  'Norway': 4.1,
  'France': 4.0,
  'Netherlands': 3.7,
}

# https://data.oecd.org/gdp/gross-domestic-product-gdp.htm

country_to_gdp_1980_usd = {
  'China': 308, # thousand millions
  'Korea': 91.5,
  'New Zealand': 26.5,
  'Finland': 44.1,
  'Sweden': 92.5,
  'Austria': 79.4,
  'Denmark': 50.6,
  'Norway': 40.3,
  'France': 533,
  'Netherlands': 152,
}
for key in country_to_gdp_1980_usd:
  country_to_gdp_1980_usd[key] *= 10 ** 9

country_to_agg_gdp_1980_usd = {
  country: country_to_percent_gdp_agr_1980[country] / 100 * country_to_gdp_1980_usd[country]
  for country in country_to_gdp_1980_usd
}

oecd_result = sum(country_to_agg_gdp_1980_usd.values())
print('oecd_result: ${:,}'.format(int(oecd_result)))


# http://www.fao.org/fileadmin/templates/ess/documents/GDP/IND_NewsRelease_EN__27Apr2015_.pdf
# $3.4 trillion
