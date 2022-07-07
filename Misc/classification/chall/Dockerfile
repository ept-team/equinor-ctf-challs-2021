# to run locally:
# sudo docker build -t container-name .  
# sudo docker run -p 1024:1024 --rm -it container-name

FROM python:3.8-slim-buster

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY flag.txt .
COPY data.npy .
COPY solution.npy .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN chown -R root:root /home/ctf
RUN chmod 755 ./ynetd
USER ctf

CMD [ "./ynetd", "python3 classification.py"]
