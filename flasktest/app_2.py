from flask import Flask, jsonify, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'abnegation123',
        database = 'school'
)

@app.route('/', methods = ['GET'])
def home():
    return render_template('form.html')

@app.route('/students', methods = ['GET', 'POST'])
def students():
    if request.method == 'GET':
        # create fieldnames
        curs = mydb.cursor()
        curs.execute('describe students')
        result = curs.fetchall()
        fieldnames = []
        for data in result:
            fieldnames.append(data[0])

        # fetch data
        curs.execute('select * from students')
        result = curs.fetchall()
        data = []
        for item in result:
            x = {fieldnames[0] : item[0],
                fieldnames[1] : item[1],
                fieldnames[2] : item[2]
                }
            data.append(x)
        return jsonify(data)

    elif request.method == 'POST':
        body = request.form
        # body = request.json
        curs = mydb.cursor()
        qry = 'insert into students(name, age) values(%s, %s)'
        val = (body['name'], body['age'])
        curs.execute(qry, val)
        mydb.commit()
        # return jsonify({'status': 'Data has been entered'})
        return redirect('/students')
    else:
        return jsonify({'status': 'Only GET & POST'})

# get data by id
@app.route('/students/<string:nis>')
def student(nis):
    if nis.isdigit() and int(nis)>0:
         # create fieldnames
        curs = mydb.cursor()
        curs.execute('describe students')
        result = curs.fetchall()
        fieldnames = []
        for data in result:
            fieldnames.append(data[0])

        # fetch data
        qry = 'select * from students where nis = %s'
        nis = (nis,)
        curs.execute(qry,nis)
            # or
        # curs.execute(f'select * from students where nis = {nis}')

        result = curs.fetchall()
        data = []
        for item in result:
            x = {fieldnames[0] : item[0],
                fieldnames[1] : item[1],
                fieldnames[2] : item[2]
                }
            data.append(x)
        return jsonify(data)
    else:
        return jsonify({'status': 'Please input a number bigger than 0'})


if __name__ == '__main__':
    app.run(debug=True)

