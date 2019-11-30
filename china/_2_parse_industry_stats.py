import glob, json, csv

industries = []
for path in glob.glob('china-industries/*.json'):
  with open(path) as f:
    text = f.read()
  industry_dict = json.loads(text)
  cname = industry_dict['returndata']['wdnodes'][0]['nodes'][0]['cname']
  name = cname.split('Sales of ', 1)[1].rsplit(',', 1)[0]
  units_sold = industry_dict['returndata']['datanodes'][0]['data']['data']
  industries.append((name, units_sold))

column_labels = ['name', 'units_sold']
with open('out.csv', 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  writer.writerow(column_labels)
  for industry in industries:
    writer.writerow(industry)
