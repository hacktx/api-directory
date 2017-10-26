from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import render_template
import json

app = Flask(__name__)
# set up freezer config
app.config.from_pyfile('settings.py')
# read json data
data = json.loads(open('data.json', 'r').read())

@app.route('/')
def index_page():
	if request.method == 'GET':
    	return render_template('index.html', apis=data['apis'], challenges=data['challenges'])

@app.route('/data.json')
def data_json():
    return jsonify(data)

"""
@app.route('/api/<name>.html')
def api_page(name=None):
    if name is None:
        return render_template('index.html')
    return render_template('api.html', data=data['apis'][name])
"""
