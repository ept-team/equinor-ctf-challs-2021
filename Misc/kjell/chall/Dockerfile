FROM python:3

WORKDIR /app

COPY ynetd .
COPY kjell.py .
COPY flag.txt .

RUN chmod +x ynetd

RUN useradd kjell
USER kjell

CMD ./ynetd -d /app -lt 1 -se y -p 3000 "python3 -u kjell.py"