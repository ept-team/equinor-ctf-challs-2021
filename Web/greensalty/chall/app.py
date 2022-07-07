import sqlite3
import base64
import pickle
import json
from flask import Flask, request, make_response, render_template, redirect, g, session
from flask.helpers import url_for

app = Flask(__name__)

DATABASE = 'pwn.sqlite3'
app.secret_key = 'dasjdiqw3e9123f'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS users
        ([username] TEXT, [password] TEXT, [role] TEXT)
          ''')

conn.commit()
conn.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def add_data_to_db(query, args=(), one=False):
    cur = get_db()
    cur.execute(query, args)
    cur.commit()
    cur.close()
    

class UserType(object):
    def __init__(self):
        self.role = ''
        self.name = ''


with open('flag.txt', 'r') as solution:
    flag = solution.readline()


@app.route('/', methods=['GET', 'POST'])
def index():
    resp = redirect(url_for('dashboard'))
    return resp


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('status')
    resp = redirect(url_for('login'))
    resp.set_cookie('Role', '', expires=0)
    return resp

@app.route('/dashboard.html', methods=['POST', 'GET'])
def dashboard():
    pickle_data = request.cookies.get('Role')
    message = request.args.get('message')
    if message == None:
        message = ''
    if pickle_data == None:
        resp = redirect(url_for('login'))
        return resp
    else:
        try:
            if b'R' in base64.b64decode(pickle_data):
                resp = redirect(url_for('login'))
                return resp
            else:
                try:
                    user = pickle.loads(base64.b64decode(pickle_data))
                except:
                    pass
        except:
            pass
        segment = get_segment( request )
        resp = make_response(render_template('dashboard.html', message=message, segment=segment))
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

@app.route('/transactions.html', methods=['POST', 'GET'])
def transaction():
    pickle_data = request.cookies.get('Role')
    if pickle_data == None:
        resp = redirect(url_for('login'))
        return resp
    else:
        try:
            if b'R' in base64.b64decode(pickle_data):
                resp = redirect(url_for('login'))
                return resp
            else:
                try:
                    user = pickle.loads(base64.b64decode(pickle_data))
                except:
                    resp = redirect(url_for('login'))
                    return resp
        except:
            pass
        segment = get_segment( request )
        resp = make_response(render_template('transactions.html', segment=segment))
        return resp

@app.route('/settings.html', methods=['POST', 'GET'])
def settings():
    pickle_data = request.cookies.get('Role')
    if pickle_data == None:
        resp = redirect(url_for('login'))
        return resp
    else:
        try:
            if b'R' in base64.b64decode(pickle_data):
                resp = redirect(url_for('login'))
                return resp
            else:
                try:
                    user = pickle.loads(base64.b64decode(pickle_data))
                    if user.role == 'Admin':
                        return flag
                    else:
                        message='Only Admin is allowed to change settings'
                        resp = redirect(url_for('dashboard', message=message))
                        return resp
                except:
                    pass
        except:
            pass
        resp = make_response(render_template('dashboard.html'))
        return resp



@app.route('/sign-in.html', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            row = query_db("Select * from users where username=? and password=?",[username, password],one=True)
            if row == None:
                resp = make_response(render_template('sign-in.html'))
                return resp
            if len(row) == 0 :
                resp = make_response(render_template('sign-in.html'))
                return resp
            session['status'] = 'user'
            resp = redirect(url_for('dashboard'))
            user = UserType()
            user.name = row[0]
            user.role = row[2]
            pickle_data = pickle.dumps(user)
            cookie_data = base64.b64encode(pickle_data)
            resp.set_cookie('Role',cookie_data)
            return resp
        except Exception as e:
            pass
    else:
        resp = make_response(render_template('sign-in.html'))
        return resp



@app.route('/sign-up.html', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            add_data_to_db("INSERT INTO users (username, password,role) VALUES(?,?,'EndUser')",[username, password])
        except Exception as e:
            pass
        resp = redirect(url_for('login'))
        return resp
    else:
        resp = make_response(render_template('sign-up.html'))
        return resp

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db