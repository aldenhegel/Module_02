import pymongo
import mysql.connector

dbmongo = input('Please input mongoDB db: ')
coll = input('Please input collection: ')
dbsql = input('Please input mysql db: ')
tblsql = input('Please input mysql table: ')

# mongoDB activation
user = pymongo.MongoClient('mongodb://localhost:27017')
dbmongo = user[f'{dbmongo}']
coll = dbmongo[f'{coll}']

# sql activation
mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'abnegation123',
    auth_plugin = 'mysql_native_password',
)
curs = mydb.cursor()
curs.execute(f'create database {dbsql}')
curs.execute(f'use {dbsql}')

# fetch data
datamongodb = []
field = []
for item in list(coll.find()):

    # ObjectId extraction
    item['_id'] = str(item['_id'])
    datamongodb.append(item)

    # field names extraction
    for i in item.keys():
        if i not in field:
            field.append(i)

# =================================================================================================================



# transfer data

# create table, adding columns
for item in field:
    if item == field[0]:
        curs.execute(f'create table {tblsql}({item} varchar(256))')
    else:
        curs.execute(f"alter table {tblsql} add column {item} varchar(256)")

# data insertion
for item in datamongodb:
    for item1, item2 in zip(item.keys(), item.values()):
        if item1 == field[0]:
            curs.execute(f"insert into {tblsql} ({item1}) values('{item2}')")
        else:
            curs.execute(f"update {tblsql} set {item1} = '{item2}' where {field[0]} = '{item[field[0]]}'")

mydb.commit()