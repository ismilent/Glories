from flask import Blueprint, request
from padmin.user.models import Users
from padmin.extensions import bcrypt

user_print = Blueprint('user', __name__, url_prefix='/user')

@user_print.route('/add', methods=['POST'])
def add_user():
    form = request.form
    print form
    password = bcrypt.generate_password_hash('123456')
    user = Users('admin', 'a@a.cn', password )
    user.save()
    return 'Done'
    
    