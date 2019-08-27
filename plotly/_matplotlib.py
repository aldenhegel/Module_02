from flask import Flask, request, render_template, send_from_directory, redirect
import os
from werkzeug.utils import secure_filename
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './csv'

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/uploadmatplotlib', methods = ['POST'])
def upload():
    if request.method == 'POST':
        myfile = request.files['file']
        fn = secure_filename(myfile.filename)
        myfile.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        return redirect('/matplotlib/' + fn)

@app.route('/matplotlib/<path:haha>')
def plotdata(haha):
    df = pd.read_csv(haha)
    plt.style.use('seaborn')
    plt.plot(df['x'], df['y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(
        'csv/matplotlib.png',
        transparent = True
        )
    return send_from_directory('csv', 'matplotlib.png')

    

if __name__ == '__main__':
    app.run(debug=True)
  
