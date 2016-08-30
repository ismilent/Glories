from flask import Blueprint, request, render_template, \
                flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from padmin.auth.forms import LoginForm
from padmin.auth.models import Users

mod_admin = Blueprint('auth', __name__, url_prefix='/auth')

@mod_admin.route('/')
def index():
    return redirect('auth/login')

@mod_admin.route('/login/', methods=['GET', 'POST'])
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

@mod_admin.route('/home/')
def home():
    return render_template('auth/dashboard.html')