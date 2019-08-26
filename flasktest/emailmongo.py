from flask import Flask, jsonify, request, render_template, redirect
import pymongo

app = Flask(__name__)

x = pymongo.MongoClient('mongodb://localhost:27017')

# create db
db = x['email']
coll = db['email']

@app.route('/')
def home():
    return render_template('email.html')

@app.route('/signup', methods = ['POST'])
def signup():
    body = request.form
    email = []
    data = list(coll.find())
    for item in data:
        email.append(item['email'])
    if body['email'] in email:
        return 'Email unavailable'
    else:
        data = {'email': body['email'], 'password': body['password']}
        coll.insert_one(data)
        return 'Sign Up successful'

@app.route('/login', methods = ['POST'] )
def login():
    body = request.form 
    data = list(coll.find())
    email = []
    password = []
    for item in data:
        email.append(item['email'])
        password.append(item['password'])
    if body['email'] in email and body['password'] in password:
        return 'Login Successful'
    elif body['email'] not in email:
        return 'Email not registered, please sign up'
    else:
        return 'Wrong password'

if __name__ == '__main__':
    app.run(debug=True)

