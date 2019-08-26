import pymongo
import json

x = pymongo.MongoClient('mongodb://localhost:27017')

db = x['marvel']
coll = db['avengers']

dictionary = list(coll.find())

for item in dictionary:
    item['_id'] = str(item['_id'])
    
with open('mongodbtojson.json', 'w') as x:
    json.dump(dictionary, x)