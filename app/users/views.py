'''
views for blueprint 'users' 
'''

from flask import render_template, redirect, session, url_for, current_app, flash, request
from flask_login import login_user, logout_user, current_user

# from models.py import User class
from ..models import User
# from ./__init__.py import blurprint "users"
from . import users
# from ./form.py import
from .form import LoginForm, RegisterForm


@users.route('/login', methods=['GET', 'POST'])
def login():
    #Use a custome LoginForm with wtf to represent and validate form datas.
    #validate_on_submit will check POST and validate required conditions.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query_by(username=form.username.data)
        if user is not None and user.verify_password(form.password.data):
            #Logs a user in. You should pass the actual user object to this. 
            #If the user’s is_active property is False, they will not be logged in unless force is True.
            #This will call User.get(user_id) return True if the log in attempt succeeds, 
            #and False if it fails (i.e. because the user is inactive).
            login_user(user, form.remember_me.data)
            flash("Logging Success!")
            return redirect(url_for('pages.index'))
        flash("Invalid Username or Password!")
    return render_template('users/login.html', form=form)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #OK to register: username and email verified within RegisterForm
        user = User(form.username.data, 
                    form.email.data, 
                    form.password.data)
        User.insert(user)
        flash("Thanks for registration!")
        #Now auto login
        user = User.query_by(username=form.username.data)
        login_user(user)
        #Redirect to Home page
        return redirect(url_for('pages.index'))
    return render_template('users/register.html', form=form)
    
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('pages.index'))
