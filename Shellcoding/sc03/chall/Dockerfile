# sudo docker build -t 01 .
# sudo docker run -d -p 1024:1024 --rm -it 01

FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY ynetd .
COPY flag.txt /opt/flag
COPY sc03 .

RUN chown -R root:root /home/ctf
RUN chmod  -R a+rx /home/ctf
USER ctf
CMD ./ynetd ./sc03
