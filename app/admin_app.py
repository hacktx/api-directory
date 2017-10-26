from flask import Flask
from flask import jsonify
from flask import make_response
from flask import render_template
import json

app = Flask(__name__)
# set up freezer config
app.config.from_pyfile('settings.py')
# read json data
data = json.loads(open('data.json', 'r').read())

@app.route('/', 'dashboard')
def index_page():
    if request.method == 'GET':
    	return render_template('form.html', apis=data['apis'], challenges=data['challenges'])
	else:
        val = request.form.get('button')
        if val == 'apis':
            return apis(request)
        elif val == 'challenges':
            return challenges(request)
        else:
            return redirect(url_for('dashboard'))

def apis(request):
	api_info = {
		request.form.get('company_name'): {
			'name':request.form.get('company_name'),
			'image': request.form.get('image'),
			'description': request.form.get('description'),
			'link': request.form.get('link'),
			'keywords': [request.form.get('search_keywords')],
			'chip_keywords': [request.form.get('chip_keywords')]
			,
			'prizes': {
				request.form.get('prize_name') : request.form.get('prize')
			}
		}
	}

def challenges(request):
	challenge_info = {
		request.form.get('company_name'): {
			'name':request.form.get('company_name'),
			'image': request.form.get('image'),
			'description': request.form.get('description'),
			'link': request.form.get('link'),
			'keywords': [request.form.get('search_keywords')],
			'chip_keywords': [request.form.get('chip_keywords')]
			,
		}
	}
	update_challenge_json(challenge_info)
	return redirect(url_for('dashboard'))

	update_api_json(api_info)
	return redirect(url_for('dashboard'))	

def update_challenge_json(challenge_info):
	with open('data.json') as f:
    	data = json.load(f)
	data["challenges"].append({'b':'2'})


def update_api_json(api_info):
	with open('data.json') as f:
    	data = json.load(f)
	data["apis"].append({'b':'2'})
	


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
