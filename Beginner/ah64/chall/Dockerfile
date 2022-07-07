FROM httpd:2.4.50-alpine
#RUN adduser -u 1001 -h /home/ctf/ -s /bin/sh ctf -g "EPT{we've_got_a_blackhawk_down_we've_got_a_blackhawk_down_i_mean_apache}" --disabled-password
#RUN echo "ctf:ctf" | chpasswd

#WORKDIR /home/ctf

COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY flag.txt /opt/flag
#COPY flag.txt /home/ctf/flag

RUN chmod 755 /opt/flag
#RUN chmod 777 /home/ctf/flag


EXPOSE 8801

CMD ["httpd-foreground"]
