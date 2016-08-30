from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import DevConfig
from padmin.extensions import db
from padmin import auth

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprint(app)
    return app

def register_extensions(app):
    db.init_app(app)
    return None

def register_blueprint(app):
    app.register_blueprint(auth.views.mod_admin)

def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 404)
        return '404'
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None