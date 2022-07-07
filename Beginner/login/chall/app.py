import sqlite3
import base64
import pickle
import json
from flask import Flask, request, make_response, render_template, redirect, session
from flask.helpers import url_for


app = Flask(__name__)
app.secret_key = 'lolasl123'
conn = sqlite3.connect('pwn.sqlite3') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([username] TEXT, [password] TEXT, [role] TEXT)
          ''')
                     
conn.commit()
conn.close()

with open('flag.txt', 'r') as solution:
    flag = solution.readline()


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     resp = make_response(render_template('login.html'))
#     return resp


@app.route('/', methods=['GET', 'POST'])
def index():
    role = request.cookies.get('Role')
    if role == None:
        resp = redirect(url_for('login'))
        return resp
    segment = get_segment( request )
    resp = redirect(url_for('dashboard'))
    return resp


# Helper - Extract current page name from request 
def get_segment( request ):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment    
    except:
        return None  

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    role = request.cookies.get('Role')
    message = request.args.get('messages')
    if message == None:
        message = ''
    if role == None:
        resp = redirect(url_for('login'))
        return resp
    
    segment = get_segment( request )
    resp = make_response(render_template('dashboard.html', segment=segment, message=message))
    return resp

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']
        try:
            conn = sqlite3.connect('pwn.sqlite3') 
            c = conn.cursor()
            c.execute("Select * from users where username=? and password=?",[username, password])
            rows = c.fetchall()
            conn.close()
            if len(rows) == 0 :
                resp = make_response(render_template('layouts/login.html'))
                return resp
            row = rows[0]
            segment = get_segment( request )
            resp = redirect(url_for('dashboard'))
            resp.set_cookie('Role', row[2])
            session['status'] = 'user'

            return resp
        except Exception as e:
            pass
    else:
        resp = make_response(render_template('accounts/login.html'))
        return resp

@app.route('/logout', methods=[ 'GET'])
def logout():
    session.pop('status')
    resp = redirect(url_for('login'))
    resp.set_cookie('Role', '', expires=0)
    return resp


@app.route('/transactions', methods=[ 'GET'])
def transactions():
    segment = get_segment( request )
    resp = make_response(render_template('transactions.html', segment=segment))
    return resp

@app.route('/settings', methods=[ 'GET'])
def settings():
    role = request.cookies.get('Role')
    if role == None:
        resp = redirect(url_for('login'))
        return resp
    else:
        if role == "Admin":
            return flag
        else:
            segment = get_segment( request )
            message = 'Only admins can view settings'
            resp = redirect(url_for('dashboard', messages=message))
            return resp

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            conn = sqlite3.connect('pwn.sqlite3') 
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password,role) VALUES(?,?,'EndUser')",[username, password])
            conn.commit()
            conn.close()
        except Exception as e:
            pass
        resp = redirect(url_for('login'))
        return resp
    else:
        resp = make_response(render_template('accounts/register.html'))
        return resp

   


