'''
App Factory to create blueprints
'''

import os
from flask import Flask, Blueprint, g, current_app
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from .models import User, Mydb

#For the flask extensions, first create an instance without any app because the app is not created currently, then use extensions' init_app to make the app be related.
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
#Try sqlite3 first, ORM later
#db = SQLAlchemy()

#LoginManager Settings
login_manager = LoginManager()
#set strong, default is basic
login_manager.session_protection = 'strong'
#redirect to login if user attempts to access a login_required view without being logged in.
login_manager.login_view = 'users.login'

#Factory function
def create_app(config_name):

    #flask instance
    app = Flask(__name__)

    #config instance
    app.config.update(
            USERNAME='admin',
            PASSWORD='password'
            )
    app.config.from_object(config[config_name])

    #init exts
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    #db.init_app(app)
    Mydb.init_db(app)
    login_manager.init_app(app)

    #defined for LoginManager use to get a User object corresponding to user_id.
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    
    #Defined to close db connection at the end of the request.
    @app.teardown_appcontext
    def close_connection(error):
        if hasattr(g, '_database'):
            g._database.close()

    #register blueprints
    from .dashboard import dashboard as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    from .pages import pages as pages_bp
    app.register_blueprint(pages_bp)
    from .users import users as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')
    
    return app

