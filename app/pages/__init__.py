'''
Define blueprint "pages"
'''

from flask import Blueprint

pages = Blueprint('pages', __name__)

from . import errors, views

