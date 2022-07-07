FROM python:3.8-slim-buster 
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY requirements.txt requirements.txt
COPY templates templates
COPY static static
copy run_me.sh run_me.sh
copy secret.py secret.py
copy secret.key secret.key
COPY secret.key.pub secret.key.pub
RUN chmod 755 /home/ctf/run_me.sh
RUN chmod 755 /home/ctf/secret.key
RUN chmod 755 /home/ctf/secret.key.pub
RUN pip3 install -r requirements.txt

COPY flag.txt .
COPY app.py .

USER ctf

EXPOSE 5000

CMD [ "/home/ctf/run_me.sh"]

