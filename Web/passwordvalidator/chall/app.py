from flask import Flask, request, make_response, render_template
import string
import struct
app = Flask(__name__)


with open('flag.txt', 'r') as f:
    flag = f.readline()
      

def isValidPassword(password):
    if len(password) != 12:
        return "Incorrect password length!"
    if sum([1 for c in password if c in string.ascii_lowercase]) < 3:
        return "Not enough lowercase letter in the password!"
    if sum([1 for c in password if c in string.ascii_uppercase]) < 3:
        return "Not enough uppercase letter in the password!"
    if sum([1 for c in password if c in string.punctuation]) < 3:
        return "To few special characters in the password!"
    if sum([1 for c in password if c in string.digits]) < 3:
        return "Not enough digits in the password!"
    if len(password) > len(set(password)):
        return "All characters must be unique!"
    #sorry not sorry.
    if 0xdeadc0de != struct.unpack(">I", bytes(map(lambda l: l[0] + l[1] ^ l[2], [list(map(ord, password))[i:i+3] for i in range(0, 12, 3)])))[0]:
        return "Invalid checksum, should be 0xdeadc0de!"
    return None

@app.route('/',methods = ['POST', 'GET'])
def index():
    flagTxt = ''
    if request.method == 'POST':
        if not 'password' in request.form:
            res = "No password provided."
        else:
            password = request.form['password']
            res = isValidPassword(password)
            if not res:
                flagTxt = flag
        return render_template('index.html', flag=flagTxt, error=res)
        

    elif request.method == 'GET':
        return render_template('index.html')
    else:
        return None



# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)




