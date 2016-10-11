from flask import Flask
from flask import render_template
import json

app = Flask(__name__)
data = json.load(open('data.json', 'r'))

@app.route('/')
def index_page():
    return render_template('index.html', companies=data['companies'])

@app.route('/api/<name>')
def api_page(name=None):
    return render_template('index.html') if name is None else render_template('api.html', name=name, data=data['companies'][name])
