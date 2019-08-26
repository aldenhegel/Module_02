from flask import Flask, send_from_directory, render_template, url_for, jsonify, abort, redirect, request

import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'abnegation123',
        database = 'email'
)

@app.route('/')
def home():
    return render_template('email.html')

@app.route('/signup', methods = ['POST'])
def signup():
    body = request.form
    curs = mydb.cursor()
    curs.execute('select * from email')
    data = curs.fetchall()
    email = []
    for item in data:
        email.append(item[0])
    if body['email'] in email:
        return 'Email unavailable'
    else:
        qry = 'insert into email(email, password) values(%s,%s)'
        val = (body['email'], body['password'])
        curs.execute(qry, val)
        mydb.commit()
        return 'Sign Up successful'

    return render_template('backtohome.html')

@app.route('/login', methods = ['POST'] )
def login():
    body = request.form 
    curs = mydb.cursor()
    curs.execute('select * from email')
    data = curs.fetchall()
    email = []
    password = []
    for item in data:
        email.append(item[0])
        password.append(item[1])
    if body['email'] in email and body['password'] in password:
        return 'Login Successful'
    elif body['email'] not in email:
        return 'Email not registered, please sign up'
    else:
        return render_template('backtohome.html')
        
    

if __name__ == '__main__':
    app.run(debug=True)

