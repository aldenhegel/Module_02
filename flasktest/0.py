import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'abnegation123',
        database = 'school'
)

curs = mydb.cursor()
curs.execute('describe students')
result = curs.fetchall()
fieldnames = []
for data in result:
    fieldnames.append(data[0])


curs.execute('select * from students')
result = curs.fetchall()
data = []
for item in result:
    x = {fieldnames[0] : item[0],
        fieldnames[1] : item[1],
        fieldnames[2] : item[2]
        }
    data.append(x)

print(data)


