'''
views for blueprint dashboard
'''

from flask import render_template, redirect, session, url_for, current_app
# from ./__init__.py import blurprint
from . import dashboard
# from ./form.py import a function
#from .form import proc_name

@dashboard.route('/dashboard')
def index():
    return "welcome to dashboard!"
