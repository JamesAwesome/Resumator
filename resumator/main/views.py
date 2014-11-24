import os

from . import main
from .errors import ResumeNotFound

from urllib.parse import urlparse
from urllib.request import urlopen

from flask import json, jsonify, current_app 


@main.route('/')
def index():
    resume_json = get_resume(current_app.config['RESUME_JSON'])
    return jsonify(resume_json)

def get_resume(location):
    if os.path.isfile(location):
        with open(location, 'r') as resume:
            return json.loads(resume.read())

    elif urlparse(location).scheme in ['http', 'https']:
        with urlopen(location) as resume:
            return json.loads(resume.read())

    else:
        raise ResumeNotFound
