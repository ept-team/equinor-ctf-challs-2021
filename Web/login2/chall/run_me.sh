#!/bin/bash
set -m

#python3 /home/ctf/secret.py &
export FLASK_APP=secret
python3 -m flask run --host=127.0.0.1 --port=8000 &
export FLASK_APP=app
python3 -m flask run --host=0.0.0.0 --port=5000