import os

from . import main
from .errors import ResumeNotFound

from urllib.parse import urlparse
from urllib.request import urlopen

from flask import json, jsonify, current_app, render_template, request
from flask_weasyprint import HTML, render_pdf

@main.route('/')
@main.route('/<format>')
def index(format=None):
    resume_json = get_resume(current_app.config['RESUME_JSON'])
    user_agent = request.user_agent.string

    if format == 'raw' or (user_agent.startswith('curl/') and format == None):
        return jsonify(resume_json)
  
    html = render_template('resume.html', resume=resume_json)
    if format in [None, 'html']:
        return html
    elif format == 'pdf':
        return render_pdf(HTML(string=html))
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
