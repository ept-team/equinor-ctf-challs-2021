from flask import Flask, render_template, url_for, abort, request, redirect, make_response
import sys
import os
from base64 import b64encode
from waitress import serve

app = Flask(__name__)
flag = open("flag.txt", "r").read()

@app.route('/', methods=['GET'])
def index():
    return make_response(render_template('index.html', flag=b64encode(flag.encode()).decode()))

if __name__ == '__main__':
    if sys.platform.lower() == "win32": 
        os.system('color')
    serve(app, port=1234, host="0.0.0.0")
