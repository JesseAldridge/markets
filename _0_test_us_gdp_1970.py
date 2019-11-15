import _0_parse_oecd

# https://www.google.com/search?q=us+gdp+1970
google_result = 1.076 * 10 ** 6
# https://data.oecd.org/pinboard/4sBF
oecd_result = 1.07 * 10 ** 6
my_result = _0_parse_oecd.get_country_by_year_to_gdp()['USA'][1970]
for result in [google_result, oecd_result]:
  off_by_percent = abs(result - my_result) / my_result
  print '{:,}'.format(result)
  print 'off by: {}%'.format(round(off_by_percent, 4))
  assert off_by_percent < .01
print 'looks good'
