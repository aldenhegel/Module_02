import json
import csv

# readjson
with open('cvsjson.json') as x:
    data = json.load(x)
print(data)

# writejson
with open('cvsjson.json','w') as x:
    json.dump(data,x)

# write csv
with open('cvsjson.csv','w') as x:
    column=list(data[0].keys())
    write=csv.DictWriter(x,fieldnames=column)
    write.writeheader()
    write.writerows(data)

# read csv
data=[]
with open ('cvsjson.csv','r') as x:
    reader=csv.DictReader(x)
    for item in reader:
        data.append(dict(item))
with open('cvsjson.json','w') as x:
    json.dump(data,x)
    