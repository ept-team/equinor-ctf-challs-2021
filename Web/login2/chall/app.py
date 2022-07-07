import sqlite3
import base64
import pickle
import json
import jwt
import requests
from flask import Flask, request, make_response, render_template, redirect, session
from flask.helpers import url_for
from waitress import serve

PRIVATE_KID = "http://localhost:8000/secret"
PUBLIC_KID = "http://localhost:8000/secret2"

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

def get_private_key(kid):
    resp = requests.get(kid)
    return resp.content

@app.route('/', methods=['GET', 'POST'])
def index():
    segment = get_segment( request )
    resp = make_response(render_template('login.html', segment=segment))
    return resp

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('status')
    resp = redirect(url_for('login'))
    resp.set_cookie('Role', '', expires=0)
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

@app.route('/dashboard.html', methods=['POST', 'GET'])
def dashboard():
    encoded = request.cookies.get('Role')
    message = request.args.get('message')
    if message == None:
        message = ''
    try:
        headers = jwt.get_unverified_header(encoded)
        secret_key = get_private_key(headers['kid'])
        values = jwt.decode(encoded, secret_key, algorithms=['RS256'])
        role = values['Role']
    except Exception as e:
        pass
    try:
        if role == None:
            resp = redirect(url_for('login'))
            return resp
        else:
            if role == "Admin":
                return flag
            else:
                segment = get_segment( request )
                resp = make_response(render_template('index.html', segment=segment, is_authenticated = True, message=message))
                return resp
    except Exception as e:
        resp = redirect(url_for('login'))
        return resp

@app.route('/login.html', methods=['POST', 'GET'])
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
                resp = make_response(render_template('login.html'))
                return resp
            row = rows[0]
            session['status'] = 'user'
            resp = redirect(url_for('dashboard'))
            encoded = jwt.encode({"Username":row[0],"Role": row[2]}, get_private_key(PRIVATE_KID), algorithm="RS256",headers={"kid": PUBLIC_KID})
            resp.set_cookie('Role', encoded)
            
            return resp
        except Exception as e:
            pass
    else:
        segment = get_segment( request )
        resp = make_response(render_template('login.html', segment=segment, is_authenticated = False))
        return resp

@app.route('/notifications.html', methods=['GET'])
def notifications():
    encoded = request.cookies.get('Role')
    try:
        headers = jwt.get_unverified_header(encoded)
        secret_key = get_private_key(headers['kid'])
        values = jwt.decode(encoded, secret_key, algorithms=['RS256'])
        role = values['Role']
    except Exception as e:
        pass
    try:
        if role == None:
            resp = redirect(url_for('login'))
            return resp
        else:
            if role == "Admin":
                return flag
            else:
                segment = get_segment( request )
                message = 'Only admins can view notifications'
                resp = redirect(url_for('dashboard', segment=segment, is_authenticated = True, message=message))
                return resp
    except Exception as e:
        resp = redirect(url_for('login'))
        return resp


@app.route('/register.html', methods=['POST', 'GET'])
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
        segment = get_segment( request )
        resp = make_response(render_template('register.html', segment=segment,  is_authenticated = False))
        return resp

if __name__ == '__main__':
    serve(app, listen='0.0.0.0:5000', threads=100)
