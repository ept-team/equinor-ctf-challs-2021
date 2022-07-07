FROM python:3

WORKDIR /app

COPY ynetd .
COPY kalk.py .
COPY flag.txt .

RUN chmod +x ynetd

RUN useradd kalk
USER kalk

CMD ./ynetd -d /app -lt 1 -se y -p 3000 "python3 -u kalk.py"