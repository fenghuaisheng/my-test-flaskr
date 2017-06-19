'''
views for blueprint dashboard
'''

from flask import render_template, redirect, session, url_for, current_app
# from ./__init__.py import blurprint
from . import pages
# from ./form.py import a function
#from .form import proc_name

@pages.route('/')
def index():
    return render_template('pages/docs.html')

@pages.route('/login')
def login():
    return render_template('pages/login.html')

