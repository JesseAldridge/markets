import _0_parse_oecd

# https://en.wikipedia.org/wiki/Gross_world_product
wikipedia_result_1990_USD = 12.1 * 10 ** 12 # 1990 USD
# http://www.in2013dollars.com/1990-dollars-in-1970?amount=12.10
wikipedia_result = 3.59 * 10 ** 12 # 1970 USD

# https://data.oecd.org/pinboard/4sBF
oecd_result = 3.2 * 10 ** 12 # 1970 USD

country_by_year_to_gdp = _0_parse_oecd.get_country_by_year_to_gdp()
countries = country_by_year_to_gdp.keys()
gdps_1970_USD1970 = [country_by_year_to_gdp[country].get(1970, 0) * 10**6 for country in countries]
my_result = sum(gdps_1970_USD1970) # 1970 USD
print 'my_result: ${:,}'.format(my_result)
for result in [wikipedia_result, oecd_result]:
  off_by_percent = abs(result - my_result) / my_result
  print 'other result: {:,}'.format(result)
  print 'off by: {}%'.format(round(off_by_percent, 4))
  assert off_by_percent < .5
print 'looks good'
