from flask import Flask, request
import sys,os,os.path
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

app = Flask(__name__)

@app.route('/offline-encryption', methods=["GET", "POST"])
def encrypt():
    payload = request.data.decode()
    plaintext = pad(base64.b64decode(payload.split("plaintext=")[1].split("&")[0]), AES.block_size)
    key = base64.b64decode(payload.split("key=")[1].split("&")[0])

    iv = get_random_bytes(16)
    encrypted_noise = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
    encrypted_plaintext = AES.new(key=key, iv=iv, mode=AES.MODE_OFB)
    return base64.b64encode(iv + encrypted_noise.encrypt(bytearray(len(plaintext))) + encrypted_plaintext.encrypt(plaintext))

if __name__ == '__main__':
    if sys.platform.lower() == "win32": 
        os.system('color')
    app.run(port=9443, host="0.0.0.0", ssl_context='adhoc')