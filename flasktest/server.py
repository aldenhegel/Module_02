from flask import Flask, send_from_directory, render_template, url_for, jsonify, abort, redirect, request

import os

from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './img'

# home route
@app.route('/')
def home():
    # return render_template('home.html')
    return render_template('upload.html')

# error 404
@app.errorhandler(404)
def notFound(error):
    return '<h1>Sorry, not found</h1>'

# home route 2
@app.route('/home')
def home2():
    return redirect('/')

# api
@app.route('/api', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def api():
    if request.method == 'GET':
        return jsonify({'status': 'Anda nge-GET'})
    elif request.method == 'POST':
        # return jsonify({'status': 'Anda nge-POST'})
        body = request.json 
        # print(body['name'])
        # print(body['age'])
        return jsonify({
                'status': 'data successfully sent',
                'name': body['name'],
                'age': body['age']
                })

    elif request.method == 'PUT':
        return jsonify({'status': 'Anda nge-PUT'})
    elif request.method == 'DELETE':
        return jsonify({'status': 'Anda nge-DELETE'})
    else:
        return jsonify({'status': 'Anda lainnya'})

# post route
@app.route('/form', methods = ['POST'])
def form():
    data = request.form
    print(data['name'])
    return render_template(
                    'result.html',
                    data = data
                            )
# access file route
@app.route('/fileku/<path:haha>')
def fileaccess(haha):
    return send_from_directory('img', haha)

# upload route
@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        myfile = request.files['file']
        fn = secure_filename(myfile.filename)
        myfile.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        return redirect('/fileku/' + fn)



if __name__ == '__main__':
    app.run(debug = True)