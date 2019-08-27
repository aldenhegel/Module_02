from flask import Flask, request, render_template, send_from_directory, redirect
import os
from werkzeug.utils import secure_filename
import csv
import plotly
import chart_studio.plotly as py 
import plotly.graph_objects as go 
import json 

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './csv'

# home
@app.route('/')
def home():
        return render_template('upload.html')


# display plotly
@app.route('/showplotly/<path:haha>')
def showgraph(haha):
        x = []
        y = []
        fieldnames = []

        with open('./csv/' + haha, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for item in reader:
                        for item1 in dict(item).keys():
                                fieldnames.append(item1)
                        break
                for item in reader:
                        x.append(dict(item)[fieldnames[0]])
                        y.append(dict(item)[fieldnames[1]])

        plot = go.Scatter(x = x, y = y)
        plot = [plot]
        plotjson = json.dumps(plot, cls = plotly.utils.PlotlyJSONEncoder)
        return render_template('plotly.html', x = plotjson)

# upload route
@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        myfile = request.files['file']
        fn = secure_filename(myfile.filename)
        myfile.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        return redirect('/showplotly/' + fn)


if __name__ == '__main__':
    app.run(debug=True)