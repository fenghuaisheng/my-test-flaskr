'''
App Factory to create blueprints
'''

from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

# For the flask extensions, first create an instance without any app because the app is not created currently, then use extensions' init_app to make the app be related.
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()

# Factory function
def create_app(config_name):

    # flask instance
    app = Flask(__name__)

    # config instance
    app.config.update(
            USERNAME='admin',
            PASSWORD='password'
            )
    app.config.from_object(config[config_name])

    # init exts
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    # register blueprints
    from .dashboard import dashboard as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    #from .pages import pages as pages_bp
    #app.register_blueprint(pages_bp)
    
    return app
