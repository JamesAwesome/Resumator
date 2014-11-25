from flask import Flask
from flask.ext.misaka import Misaka

from config import config
from .main import main as main_blueprint

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_blueprint)
    Misaka(app, tables=True, wrap=True)
    return app 
