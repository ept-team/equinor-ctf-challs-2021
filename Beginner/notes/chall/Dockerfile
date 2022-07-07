FROM python:3.8-slim-buster 
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY requirements.txt requirements.txt
COPY templates templates
COPY static static
COPY forms.py forms.py
COPY models.py models.py
RUN pip3 install -r requirements.txt

COPY flag.txt .
COPY app.py .

USER ctf

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
