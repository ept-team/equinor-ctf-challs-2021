FROM python:3.8-slim-buster 
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY requirements.txt requirements.txt
COPY templates templates
RUN pip3 install -r requirements.txt

COPY flag.txt .
COPY app.py .
#RUN chown -R root:root /home/ctf

USER ctf

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]