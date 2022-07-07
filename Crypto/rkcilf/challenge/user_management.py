from models import User
import hashlib
import base64
from flask import render_template, url_for, request, redirect, make_response, abort

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f"sqlite:///prod.sqlite3")
sql_session_maker = sessionmaker(bind=engine)
sql_session = sql_session_maker()

def validate_login(username, password):
    if not (username and password):
            abort(400)
    password = base64.b64encode(hashlib.sha512(password.encode('utf-8')).digest())

    try:
        _username, _permissions  = None, None
        sql_session = sql_session_maker()
        user = sql_session.query(User).filter_by(username=username,password=password).first()
        if user:
            _username, _permissions = user.username, user.permissions
        sql_session.commit()
    except Exception as e:
        print (e)
        abort(400)
    return _username, _permissions 

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user_object = User()
            user_object.username = username
            user_object.password = base64.b64encode(hashlib.sha512(password.encode('utf-8')).digest())
            user_object.permissions = "0"
            if username == "admin":
                user_object.permissions = "1"
            sql_session = sql_session_maker()
            user = sql_session.query(User).filter_by(username=username).first()
            if user == None:
               sql_session.add(user_object)
               sql_session.commit()
            else:
                message = 'This user is already registered'
                resp = make_response(render_template('register.html',msg=message))
                return resp
        except Exception as e:
            sql_session.rollback()
            pass
        resp = redirect(url_for('login'))
        return resp
    else:
        resp = make_response(render_template('register.html'))
        return resp

def register_default_user(username, password, permissions):
    try:
        user_object = User()
        user_object.username = username
        user_object.password = base64.b64encode(hashlib.sha512(password.encode('utf-8')).digest())
        user_object.permissions = permissions
        sql_session = sql_session_maker()
        user = sql_session.query(User).filter_by(username=username).first()
        if user == None:
            sql_session.add(user_object)
            sql_session.commit()
        else:
            print('This user is already registered')
    except Exception as e:
        sql_session.rollback()
        print (e)

register_default_user("admin", "73B_EDzTsaa_ddadfd4", "1")
register_default_user("demo", "73B_EDzTsaa_ddadfd4", "0")