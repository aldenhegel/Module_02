import pymongo
import csv

user = pymongo.MongoClient('mongodb://localhost:27017')
db = input('Please input the name of the database: ')
coll = input('Please input the name of the collection: ')
csv_file = input('Please input csv file: ')

# create db and coll
db = user[f'{db}']
coll = db[f'{coll}']

# fetch data
data = []
with open(csv_file, 'r') as x:
    reader = csv.DictReader(x)
    for item in reader:
        data.append(dict(item))

# insert data
coll.insert_many(data)
