import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    VERSION = '0.1.2'
    DEBUG = True
    DEFAULT = True
    RESUME_JSON = os.environ.get('RESUME_JSON')

class TestingConfig(Config):
    TESTING = True
    RESUME_JSON = os.path.join(basedir, 'tests/fixtures/resume.json')

config = {
        'default': Config,
        'testing': TestingConfig
        }
