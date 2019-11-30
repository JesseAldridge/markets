import os, json

import requests

with open('china_industry_urls.txt') as f:
  text = f.read()

if not os.path.exists('data/china-industries'):
  os.makedirs('data/china-industries')

urls = text.splitlines()
for i, url in enumerate(urls):
  print('{}/{}'.format(i, len(urls)))
  resp = requests.get(url)
  with open('data/china-industries/{}.json'.format(url.split('k1=', 1)[-1]), 'w') as f:
    f.write(json.dumps(resp.json(), indent=2))

# http://data.stats.gov.cn/english/easyquery.htm?m=QueryData&dbcode=hgjd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A030105%22%7D%5D&k1=1574393874365
# http://data.stats.gov.cn/english/easyquery.htm?m=QueryData&dbcode=hgjd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A030101%22%7D%5D&k1=1574394081794
# http://data.stats.gov.cn/english/easyquery.htm?m=QueryData&dbcode=hgjd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A030102%22%7D%5D&k1=1574394150236
