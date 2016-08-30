from flask import Blueprint
from padmin.user.models import Users
from padmin.extensions import bcrypt

user_print = Blueprint('user', __name__, url_prefix='/user')

@user_print.route('/add')
def add_user():
    form = request.form
    
    