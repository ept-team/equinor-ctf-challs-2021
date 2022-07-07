from flask import Flask, request, make_response, render_template, redirect
from waitress import serve

app2 = Flask(__name__)

@app2.route('/secret', methods=['GET'])
def private():
    with open('secret.key','r') as secret_key:
        key = secret_key.read()
        return key

@app2.route('/secret2', methods=['GET'])
def public():
    with open('secret.key.pub','r') as secret_key:
        key = secret_key.read()
        return key


if __name__ == '__main__':
    serve(app2, listen='0.0.0.0:8000', threads=100)