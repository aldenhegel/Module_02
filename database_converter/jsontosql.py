import mysql.connector
import json

db = input('Please input the name of the database: ')
table = input('Please input name of the table: ')
json_file = input('Choose json file you want to convert: ')

mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'abnegation123',
    auth_plugin = 'mysql_native_password',
)

# fetch data
field = []
with open (json_file,'r') as x:
    data = json.load(x)
    for item, stop in zip(data, range(1)):
        f_names = tuple(item.keys())
    field.append(f_names)
print(data)
print(field)


# create and use db
curs = mydb.cursor()
curs.execute(f'create database {db}')
curs.execute(f'use {db}')


# create table
qcreatetbl = f'create table {table}({field[0][0]} varchar(256))'
curs.execute(qcreatetbl)
mydb.commit()

# transfer data
for i in field[0]:
    if i != field[0][0]:
        qcreatecol = f'alter table {table} add column {i} varchar(256)'
        curs.execute(qcreatecol)
        for j in data:
            qupdate = f"update {table} set {i} = '{j[i]}' where {field[0][0]} = '{j[field[0][0]]}'"
            curs.execute(qupdate)
    else:
        for j in data:
            qinsert = f"insert into {table}({i}) values('{j[i]}')"
            curs.execute(qinsert)

mydb.commit()