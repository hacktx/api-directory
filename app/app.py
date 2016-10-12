from flask import Flask
from flask import render_template
import json

app = Flask(__name__)
# set up freezer config
app.config.from_pyfile('settings.py')
# read json data
raw_json = open('data.json', 'r').read()
data = json.loads(raw_json)

@app.route('/')
def index_page():
    return render_template('index.html', companies=data['companies'])

@app.route('/data.json')
def data_json():
    return raw_json

@app.route('/api/<name>')
def api_page(name=None):
    if name is None:
        return render_template('index.html')
    return render_template('api.html', name=name, data=data['companies'][name])
