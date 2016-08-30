from flask import Flask, render_template
from config import DevConfig
from padmin.extensions import db, login_manager, bcrypt
from padmin import auth, user

#create flask app
def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprint(app)
    return app

#Register extensions
def register_extensions(app):
    db.init_app(app)
    '''
    with app.test_request_context():
        db.create_all()
    '''
    db.app = app # if you wanna auto create table, you must db.app = app
    db.create_all()
    bcrypt.init_app(app)
    return None

#register blueprint
def register_blueprint(app):
    app.register_blueprint(auth.views.auth_print)
    app.register_blueprint(user.views.user_print)

def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 404)
        return '404'
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None