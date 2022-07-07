FROM python:3

WORKDIR /app

COPY ynetd .
COPY hedgehog.py .
COPY files files

RUN chmod +x ynetd

RUN useradd hedgehog
USER hedgehog

WORKDIR /app/files

CMD /app/ynetd -d /app/files -lt 1 -se y -p 3000 "python3 -u /app/hedgehog.py"