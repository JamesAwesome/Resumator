import os

from . import main
from .errors import ResumeNotFound

from urllib.parse import urlparse
from urllib.request import urlopen

from flask import json, jsonify, current_app 


@main.route('/')
def index():
    with get_resume(current_app.config['RESUME_JSON']) as resume:
        resume_json = json.load(resume)
        return jsonify(resume_json)

def get_resume(location):
    if os.path.isfile(location):
        return open(location, 'r')

    elif urlparse(location).scheme in ['http', 'https']:
        return urlopen(location)

    else:
        raise ResumeNotFound
