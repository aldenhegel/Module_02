import json
import csv

with open('data.json','r') as item:
    dictionary=json.load(item)
    print(dictionary)

with open('json.csv','w') as x:
    writer=csv.DictWriter(x, fieldnames=['nama','usia'])
    writer.writeheader()
    writer.writerows(dictionary)