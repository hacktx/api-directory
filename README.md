# hacktx-api-directory
Searchable directory of APIs from companies sponsoring HackTX.

# Setup
Virtualenv is highly recommended to manage dependencies. This code uses Frozen-Flask to automatically generate the static pages for hosting on Github Pages. To change the APIs available, you can either directly edit the ```app/data.json``` file (not the one at the root level of the directory), or run the admin_app.py app

## To install on a Unix system:
In the root level of your cloned directory:
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to add APIs and Challenges to the api-directory JSON
In the root level of your cloned directory:
```bash
cd app
export FLASK_APP=admin_app.py
python -m flask run
```
You should then be able to access a web interface to input the API and Challenges for the companies.

IMPORTANT: Please make sure to upload your image files to the /app/static/img/ files directory so that the company image will show.

Sometimes, you will be unable to quit your instance. In order to kill the instance, make sure to do
```bash
ps
...
4762 ttys000    0:00.26 python -m flask run
..
```
and kill the pid that is associated to ```python -m flask run```
Ex:
```bash
kill <pid>
```

## How to create static files
When you are done with adding all your APIs/Challenges, make sure you're in the /app directory and run
```bash
python freezer.py
```
This will populate the data.json file outside of /app and update index.html to contain all the api and challenge information.

