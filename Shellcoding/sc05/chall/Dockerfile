# sudo docker build -t 01 .
# sudo docker run -d -p 1024:1024 --rm -it 01

FROM ubuntu:20.04

RUN apt-get update && apt-get -y install cron python3

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf


COPY ynetd .
COPY flag.txt /root/flag.txt
COPY generateFiles.py /opt
COPY sc05 .

RUN chown -R root:root /home/ctf
RUN chmod  -R a+rx /home/ctf

COPY cronjob.txt /etc/cron.d/hello-cron
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Apply cron job
RUN crontab /etc/cron.d/hello-cron
 
# Create the log file to be able to run tail
RUN touch /var/log/cron.log
 
# Run the command on container startup
CMD cron && tail -f /var/log/cron.log