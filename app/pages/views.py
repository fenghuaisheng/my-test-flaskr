'''
views for blueprint dashboard
'''

from flask import render_template, redirect, session, url_for, current_app, flash, request
from flask_login import login_required
#from ./__init__.py import blurprint "pages"
from . import pages

@pages.route('/')
def index():
    return render_template('pages/index.html')

@pages.route('/docs', methods=['GET', 'POST'])
@login_required
def show_docs():
    return render_template('pages/docs.html')
