from flask import Blueprint, request, render_template, \
                flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from padmin.auth.forms import LoginForm
from padmin.user.models import Users

auth_print = Blueprint('auth', __name__, url_prefix='/auth')

@auth_print.route('/')
def index():
    return redirect('auth/login')

@auth_print.route('/login/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if 'isLogin' in session and session['isLogin'] == True:
        return redirect(url_for('auth.home'))

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['isLogin'] = True
            flash('Welcome %s' % user.username)
            return redirect(url_for('auth.home'))
        flash('Wrong email or password', 'error-message')
    return render_template('auth/login.html', form=form)

@auth_print.route('/home/')
def home():
    return render_template('auth/dashboard.html')