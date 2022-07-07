FROM python:3.8-slim-buster

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

USER ctf
EXPOSE 1234
CMD [ "python3",  "server.py"]

