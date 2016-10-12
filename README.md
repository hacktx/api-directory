# hacktx-api-directory
Searchable directory of APIs from companies sponsoring HackTX.
# Setup
Virtualenv is highly recommended to manage dependencies. This code uses Frozen-Flask to automatically generate the static pages for hosting on Github Pages. To change the APIs available, you can edit the ```app/data.json``` file (not the one at the root level of the directory).
## To install on a Unix system:
In the root level of your cloned directory:
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Then, edit ```app/data.json``` as you please. When you are done, run
```bash
cd app
python freezer.py
```
