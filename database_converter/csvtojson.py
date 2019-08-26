import json
import csv

dictjson=[]
with open('json.csv','r') as x:
    reader=csv.DictReader(x)
    for i in reader:
        dictjson.append(dict(i))

with open('data.json','w') as item:
    a=str(dictjson).replace("'",'"')
    item.write(a)

    


