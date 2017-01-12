from flask_wtf import FlaskForm
from wtforms import  PasswordField, StringField, validators
from wtforms.validators import  Email, EqualTo, DataRequired, Length

class LoginForm(FlaskForm):
    email = StringField('Email Address', [Email(), DataRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [DataRequired(message='Must provide a password.')])

class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired(message='Need'),Length(min=4, max=25)])
    email = StringField('Email', [Email(), DataRequired(message='Need'), Length(min=4, max=25)])
    password = PasswordField('New Password', [DataRequired(), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Repeat Password', [DataRequired()])