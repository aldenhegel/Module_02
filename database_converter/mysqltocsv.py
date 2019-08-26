import mysql.connector
import csv

database = input('Please enter database you want to use: ')
mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'abnegation123',
    auth_plugin = 'mysql_native_password',
    database = database
)
# fetch data
table = input('Please enter table you want to use: ')
curs = mydb.cursor()
querydb = 'describe ' + table
curs.execute(querydb)
tuplesfieldnames = curs.fetchall()
querydb2 = 'select * from ' + table
curs.execute(querydb2)
tuplesdata = curs.fetchall()

# create dict
dictionary = []
for item in tuplesdata:
    d = {}
    for item1, item2 in zip(tuplesfieldnames, item):
        d[item1[0]] = item2
    dictionary.append(d)

# transfer to csv
fieldnames = []
for item in tuplesfieldnames:
    fieldnames.append(item[0])
with open('mysqltocsv.csv','w') as x:
    writer = csv.DictWriter(x, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(dictionary)


