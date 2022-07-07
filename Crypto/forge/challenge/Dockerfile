# sudo docker build -t forge .
# sudo docker run -d -p 1234:1234 --rm -it forge


FROM python:3.8-slim-buster

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

USER ctf

CMD [ "python3",  "server.py"]

