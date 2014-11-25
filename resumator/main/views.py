import os

from . import main
from .errors import ResumeNotFound

from urllib.parse import urlparse
from urllib.request import urlopen

from flask import json, jsonify, current_app, render_template

@main.route('/')
@main.route('/<format>')
def index(format=None):
    resume_json = get_resume(current_app.config['RESUME_JSON'])
    if format == None:
        return render_template('resume.md', resume=resume_json)
    elif format == 'raw':
        return jsonify(resume_json)
    else:
        raise ResumeNotFound('Invalid Format!')

def get_resume(location):
    # Load resume json from filepath or http(s)
    if os.path.isfile(location):
        with open(location, 'r') as resume:
            return json.loads(resume.read())

    elif urlparse(location).scheme in ['http', 'https']:
        with urlopen(location) as resume:
            return json.loads(resume.read())

    else:
        raise ResumeNotFound
