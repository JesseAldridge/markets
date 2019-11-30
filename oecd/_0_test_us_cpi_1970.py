import _0_parse_oecd

cpi_1980 = _0_parse_oecd.get_year_to_cpi()[1980]

# https://data.oecd.org/price/inflation-cpi.htm?context=OECD
oecd_value = 18.8

print('my result:', cpi_1980)
print('oecd_value:', oecd_value)
assert abs(cpi_1980 - oecd_value) / oecd_value < .01
