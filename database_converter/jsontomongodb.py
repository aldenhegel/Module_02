import pymongo
import json

user = pymongo.MongoClient('mongodb://localhost:27017')
db = input('Please input the name of the database: ')
coll = input('Please input the name of the collection: ')
json_file = input('Please input json file: ')

# create db and coll
db = user[f'{db}']
coll = db[f'{coll}']

# fetch data
with open(json_file, 'r') as x:
    data = json.load(x)

# insert data
coll.insert_many(data)