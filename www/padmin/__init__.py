from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return '404'

login_manager = LoginManager()
login_manager.setup_app(app)

@login_manager.user_loader
def load_user(userid):
    return 

from app.auth.views import mod_admin as admin_module
app.register_blueprint(admin_module)
db.create_all()