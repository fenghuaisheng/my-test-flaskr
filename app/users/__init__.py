'''
Define blueprint "users" to manage user account/session...
'''

from flask import Blueprint

users = Blueprint('users', __name__, url_prefix='/users')

from . import errors, views

