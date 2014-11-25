import os
import unittest
from unittest.mock import patch
import json

from resumator import create_app
from resumator.main.errors import ResumeNotFound

basedir = os.path.abspath(os.path.dirname(__file__))

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_html_resume(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_raw_resume(self):
        resume_file = os.path.join(basedir, 'fixtures/resume.json')
        with open(resume_file, 'r') as resume:
            test_json = json.load(resume)
        
            response = self.client.get('/raw')

            response_json = json.loads(response.data.decode())
            assert response_json == test_json

    def test_invalid_resume_format(self):
        response = self.client.get('/invalid_format')
        assert response.status_code == 404
        assert response.data.decode() == 'Invalid Format!'

    def test_resume_not_found(self):
        self.app.config['RESUME_JSON'] = 'non-existent'
        response = self.client.get('/raw')
        assert response.status_code == 404
        assert response.data.decode() == 'Resume Not Found!'

    @patch('resumator.main.views.urlopen')
    def validate_web_resume(self, url, urlopen_mock):
        resume_file = os.path.join(basedir, 'fixtures/resume.json')
        self.app.config['RESUME_JSON'] = url

        with open(resume_file, 'r') as resume:
            with open(resume_file, 'r') as mock_resume:

                urlopen_mock.return_value = mock_resume
                
                response = self.client.get('/raw')

                test_json = json.load(resume)
                response_json = json.loads(response.data.decode())
                assert response_json == test_json

    def test_http_resume(self):
        self.validate_web_resume('http://example.com/resume')

    def test_https_resume(self):
        self.validate_web_resume('https://example.com/resume')

    def test_resume_not_found_exception(self):
        exception = ResumeNotFound()
        assert exception.status_code == 404
        assert str(exception) == 'Resume Not Found!'

    def test_resume_not_found_custom_detail(self):
        exception = ResumeNotFound('Custom Detail!')
        assert str(exception) == 'Custom Detail!'
