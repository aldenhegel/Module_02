import mysql.connector
import pymongo


dbsql = input('Please input mysql db: ')
tblsql = input('Please input mysql table: ')
dbmongo = input('Please input mongoDB db: ')
coll = input('Please input collection: ')

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
    database = dbsql
)
curs = mydb.cursor()

# fetch data
querydb = 'describe ' + tblsql
curs.execute(querydb)
tuplesfieldnames = curs.fetchall()

querydb2 = 'select * from ' + tblsql
curs.execute(querydb2)
tuplesdata = curs.fetchall()


# create dict
datamongodb = []

for item in tuplesdata:
    dictionary = {}
    for item1, item2 in zip(tuplesfieldnames, item):
        dictionary[item1[0]] = item2
    datamongodb.append(dictionary)

# transfer to mongodb
coll.insert_many(datamongodb)

print(list(coll.find()))

