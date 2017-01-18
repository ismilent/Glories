from flask import Flask, render_template
#from aaconfig import DevConfig
from padmin.extensions import db, login_manager, bcrypt
from padmin import auth, user, home, tasks

from config import DevConfig

#create flask app
def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprint(app)
    register_errorhandlers(app)
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
    login_manager.init_app(app)
    return None

#register blueprint
def register_blueprint(app):
    app.register_blueprint(auth.views.auth_print)
    app.register_blueprint(user.views.user_print)
    app.register_blueprint(home.views.home_print)
    app.register_blueprint(tasks.views.tasks_print)


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

#app = create_app()