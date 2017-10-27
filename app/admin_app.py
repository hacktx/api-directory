from flask import Flask
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import request
import json

app = Flask(__name__)
# set up freezer config
app.config.from_pyfile('settings.py')
# read json data
data = json.loads(open('data.json', 'r').read())

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
		return render_template('form.html')
    else:
        val = request.form.get('button')
        if val == 'apis':
            return apis(request)
        elif val == 'challenges':
            return challenges(request)
        else:
			return render_template('form.html')

def apis(request):
	api_info = {
		'name':request.form.get('company_name'),
		'image': request.form.get('image'),
		'description': request.form.get('description'),
		'link': request.form.get('link'),
		'keywords': request.form.get('search_keywords').split(','),
		'chip_keywords': request.form.get('chip_keywords').split(',')
		,
	}
	update_api_json(api_info)
	return render_template('form.html')


def challenges(request):
	challenge_info = {
		'name':request.form.get('company_name'),
		'image': request.form.get('image'),
		'link': request.form.get('link'),
		'keywords': request.form.get('search_keywords').split(','),
		'chip_keywords': request.form.get('chip_keywords').split(',')
		,
		'prizes': {
			request.form.get('prize_name') : request.form.get('prize')
		}
	}
	update_challenge_json(challenge_info)
	return render_template('form.html')


def update_challenge_json(challenge_info):
	with open('data.json') as f:
		data = json.load(f)
	data["challenges"][challenge_info['name']] = challenge_info
	with open('data.json', 'w') as f:
	    json.dump(data, f, indent=2, sort_keys=True)


def update_api_json(api_info):
	with open('data.json') as f:
		data = json.load(f)
	data["apis"][api_info['name']] = api_info
	with open('data.json', 'w') as f:
	    json.dump(data, f,indent=2, sort_keys=True)


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
