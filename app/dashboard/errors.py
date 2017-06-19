'''
error handler
use app_errorhandler instead of errorhandler
'''

from flask import render_template, url_for
from . import dashboard

@dashboard.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@dashboard.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
