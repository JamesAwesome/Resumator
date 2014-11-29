import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    VERSION = '0.2.1'
    DEBUG = True
    DEFAULT = True
    RESUME_JSON = os.environ.get('RESUME_JSON')
    CACHE_TYPE = os.environ.get('CACHE_TYPE') or 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
    CACHE_MEMCACHED_SERVERS = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
    CACHE_MEMCACHED_USERNAME = os.environ.get('MEMCACHIER_USERNAME', '')
    CACHE_MEMCACHED_PASSWORD = os.environ.get('MEMCACHIER_PASSWORD', '')

class TestingConfig(Config):
    TESTING = True
    RESUME_JSON = os.path.join(basedir, 'tests/fixtures/resume.json')
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 5

config = {
        'default': Config,
        'testing': TestingConfig
        }
