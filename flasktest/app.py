from flask import Flask, abort, jsonify, render_template, url_for
app = Flask(__name__)

employees = [
    {'id': 1, 'name': 'Andi', 'age': 21},
    {'id': 2, 'name': 'Budi', 'age': 22},
    {'id': 3, 'name': 'Caca', 'age': 23},
    {'id': 4, 'name': 'Deni', 'age': 24},
    {'id': 5, 'name': 'Euis', 'age': 25}
]

# home route
@app.route('/')
def home():
    return render_template('app.html')

# second page
@app.route('/second')
def second():
    name = 'Alden'
    job = 'student'
    address = 'BSD'
    return render_template(
        '0.html',
        data = {
            'name': name, 'job': job, 'address': address
        }
)

# data page
@app.route('/data')
def data():
    return jsonify(employees)

# route for specific data
@app.route('/data/<int:id>')
def employeesid(id):
    if id < 1 or id > len(employees):
        abort(404)
    else:
        return jsonify(employees[id-1])

# error handler
@app.errorhandler(404)
def notFound(error):
    # return '<h1>Sorry, file not found</h1>'
    # return jsonify('status not found')
    return render_template('error.html')

if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port = 4321
        )