FROM python:3.8-slim-buster 
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY requirements.txt requirements.txt
COPY templates templates
COPY static static
COPY forms.py forms.py
COPY models.py models.py
COPY pwn.sqlite3.prod pwn.sqlite3
RUN pip3 install -r requirements.txt
RUN chown ctf:ctf /home/ctf/pwn.sqlite3
RUN chmod 777 /home/ctf/pwn.sqlite3
COPY app.py .

USER ctf

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
