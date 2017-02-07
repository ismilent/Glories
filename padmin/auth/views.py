from flask import Blueprint, request, render_template, \
                flash, g, session, redirect, url_for

#from flask.ext.login import login_required, login_user, logout_user, current_user, current_app
from flask_login import login_required, login_user, logout_user, current_user
from padmin.auth.forms import LoginForm, RegisterForm
from padmin.user.models import User
from padmin.extensions import bcrypt
from padmin.extensions import login_manager

from pprint import pprint

auth_print = Blueprint('auth', __name__)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

@auth_print.route('/')
def index():
    return redirect('/login')

@auth_print.route('/login', methods=['GET', 'POST'])
def login():
    if 'isLogin' in session and session['isLogin']:
        return redirect(url_for('home.index'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['isLogin'] = True 
            login_user(user, remember=True)
            flash('Welcome %s' % user.username)
            return redirect(url_for('home.index'))
        flash('Wrong email or password', 'error-message')
    return render_template('auth/login.html', form=form)

@auth_print.route('/register', methods=['GET', 'POST'])
def register():
    print request.form
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        print form
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        user.save()
        flash('Save')
        return 'OK'
    return render_template('auth/register.html', form=form)


@auth_print.route('/logout')
@login_required
def logout():
    logout_user()
    return 'a'
'''
@auth_print.route('/test')
def test():
    user = User('admin', 'a@a.cn', bcrypt.generate_password_hash('123456'))
    user.save()
    return 'True'

@auth_print.route('/sess')
@login_required
def sess():
    if  current_user.is_anonymous:
        current_app.logger.debug('Logo out')
    return 'dsd'
'''