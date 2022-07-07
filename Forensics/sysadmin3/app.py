from flask import Flask, request, send_file
 
app = Flask(__name__)
 
@app.route('/')
def getcookie():
    try:
        if request.cookies.get('sessionToken') == 'ewogICJ1c2VybmFtZSI6ICJzeXNhZG1pbiIsCiAgInJvbGUiOiAiYWRtaW4iLAogICJleHBpcmVzIjogIm5ldmVyIiAKfQ==':
            return send_file('flag.txt')
        else:
            return "My next gen portal does not have a login form :D /Sysadmin",200
    except:
        return "oops",500
