'''
login form, register form
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError
from ..models import User

class LoginForm(FlaskForm):
    # the first arg is for label display.
    # e.g. name responses for <label>User Name</label> and <input type="text" />
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me', default=False)

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(1,64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
               'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordex = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')])
    
    #The functions named as "validate_<member>" will be called automatically when validation

    def validate_username(self, field):
        if User.query_by(username=field.data):
            raise ValidationError('Username already exists.')

    def validate_email(self, field):
        if User.query_by(email=field.data):
            raise ValidationError('Email already exists.')
