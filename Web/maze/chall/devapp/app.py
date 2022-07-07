import sqlite3
from flask import Flask, request, make_response, render_template, redirect, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user,current_user
from flask.helpers import url_for



from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from models import User, Note
from forms import NoteForm, SearchForm

from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'lkdalskdowqke120edkscklsi2q9wp'
app.permanent_session_lifetime = timedelta(days=5)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.session_protection = "basic"


engine = create_engine(f"sqlite:///pwn.sqlite3")
sql_session_maker = sessionmaker(bind=engine)
sql_session = sql_session_maker()


with open('flag.txt', 'r') as solution:
    try:
        sql_session = sql_session_maker()
        note = sql_session.query(Note).filter_by(user_id=0,id=1).first()
        sql_session.commit()
        if note is None:
            flag = solution.readline()
            note = Note(title="Admin secret note", note=flag, user_id = 0)
            sql_session = sql_session_maker()
            sql_session.add(note)
            sql_session.commit()
    except:
        pass

@app.before_request
def func():
  session.modified = True

@login_manager.user_loader
def load_user(user_id):
    sql_session = sql_session_maker()
    user = sql_session.query(User).filter_by(id=user_id).first()
    return user

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    resp = redirect(url_for('notes'))
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


@app.route('/note', methods=['POST', 'GET'])
@login_required
def note():
    form = NoteForm(request.form)
    if request.method == 'POST':
        note = Note(title=form.title.data, note=form.note.data, user_id = current_user.get_id())
        sql_session = sql_session_maker()
        sql_session.add(note)
        sql_session.commit()
        resp =  redirect(url_for('notes'))
        return resp

    else:
        note_id = request.args.get('noteid')
        read_only = False
        if note_id:
            sql_session = sql_session_maker()
            note = sql_session.query(Note).filter_by(id=note_id, user_id = current_user.get_id()).first()
            if note:
                form.title.data = note.title
                form.note.data = note.note
                form.id.data = note.id
                read_only = True
        segment = get_segment( request )
        resp =  make_response(render_template('note.html', form=form,segment=segment, read_only=read_only))
        return resp



@app.route('/notes', methods=['POST', 'GET'])
@login_required
def notes():
    
    message = request.args.get('messages')
    if message == None:
        message = ''
    
    note = Note()
    note.title = 'Demo'
    note.note = 'This is my fancy note'
    sql_session = sql_session_maker()
    notes = sql_session.query(Note).filter_by(user_id=current_user.get_id())
    
    segment = get_segment( request )
    resp = make_response(render_template('notes.html', segment=segment, message=message, note=note, notes=notes))
    return resp

@app.route('/search', methods=['POST', 'GET'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST':
        try:
            conn = sqlite3.connect('pwn.sqlite3')
            text = form.search.data
            cur = conn.cursor()
            param = '%'+ text + '%'
            sql = "SELECT id FROM notes where note like '%{0}%' ".format(text)
            cur.execute(sql)

            id = cur.fetchone()[0]
            cur.close()
            conn.close()
            resp = redirect(url_for('note',noteid = id))
            return resp
        except Exception as e:
            segment = get_segment( request )
            message = 'Something bad happend, please be nice to me!'
            resp = make_response(render_template('search.html',form=form,segment=segment,message=message))
            return resp

    segment = get_segment( request )
    resp = make_response(render_template('search.html',form=form,segment=segment))
    return resp


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']
        try:
            sql_session = sql_session_maker()
            user = sql_session.query(User).filter_by(username=username,password=password).first()
            sql_session.commit()
            if user != None:
                login_user(user)
                resp = redirect(url_for('notes'))
                return resp
            else:
                msg = 'Unable to log you in'
                resp = redirect(url_for('login', msg=msg))
                return resp
        except Exception as e:
            pass
    else:
        resp = make_response(render_template('accounts/login.html'))
        return resp

@app.route('/logout', methods=[ 'GET'])
def logout():
    logout_user()
    resp = redirect(url_for('login'))
    return resp

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user_object = User()
            user_object.username = username
            user_object.password = password
            sql_session = sql_session_maker()
            user = sql_session.query(User).filter_by(username=username).first()
            if user == None:
                sql_session.add(user_object)
                sql_session.commit()
            else:
                message = 'This user is already registered'
                resp = make_response(render_template('accounts/register.html',msg=message))
                return resp
           
           
        except Exception as e:
            sql_session.rollback()
            pass
        resp = redirect(url_for('login'))
        return resp
    else:
        resp = make_response(render_template('accounts/register.html'))
        return resp
