# Code adapted from http://stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/
import os

DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Freezer will remove extra files it didn't generate, so the files listed
# below are the relevant code we need to keep.
FREEZER_DESTINATION_IGNORE = [
    'venv/',
    'requirements.txt',
    'app/',
    '.git*',
    'LICENSE',
    'README.md']
