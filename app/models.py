'''
models
'''

import sqlite3
from flask import g, current_app
from flask_login import UserMixin

class Mydb():
    def connect_db():
        #Connect to database file
        rv = sqlite3.connect(current_app.config['DATABASE'])
        #Make the query results as namedtuples, which can access by key or index
        rv.row_factory = sqlite3.Row
        return rv

    #Normally get_db is called in view functions,
    #thus use current_app instead of app in the connect_db function
    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = Mydb.connect_db()
        return db

    #QUERY
    def query_db(sql, args=(), one=False):
        cur = Mydb.get_db().execute(sql, args)
        rv = (cur.fetchone()) if one else (cur.fetchall())
        cur.close()
        return rv if rv else None

    #INSERT/UPDATE/DELETE
    #args is a list of turples
    def update_db(sql, args=()):
        db = Mydb.get_db()
        cursor = db.cursor()
        for arg in args:
            cursor.execute(sql, arg)
        db.commit()
        cursor.close()

    #Init db for only once
    def init_db(app):
        with app.app_context():
            db = Mydb.get_db()
            with app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()


class User(UserMixin):
    #TODO - db model
    #...
    
    #id is needed by 'get' callback of flask-login

    def __init__(self, username, email, password, user_id=0):
        self.id = user_id
        self.username = username 
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        row = Mydb.query_db("select * from users where id=?", [user_id], True)
        return User(row['name'], row['email'], row['password'], row['id']) if row else None
    
    #This shall use the User instance from query
    def verify_password(self, password):
        return True if self.password == password else False

    @staticmethod
    def query_by(username=None, email=None):
        if username is not None:
            row = Mydb.query_db("select * from users where name=?", [username], True)
        elif email is not None:
            row = Mydb.query_db("select * from users where email=?", [email], True)
        return User(row['name'], row['email'], row['password'], row['id']) if row else None

    @staticmethod
    def insert(user):
        args = [(user.username, user.email, user.password)]
        Mydb.update_db("insert into users(name, email, password) values(?,?,?)", args)
