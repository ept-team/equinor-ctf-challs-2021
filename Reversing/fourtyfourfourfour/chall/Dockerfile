FROM python:3.8-slim-buster

WORKDIR /app

COPY word.cab /app/
COPY word.html /app/



 EXPOSE 80

CMD [ "python3", "-m" , "http.server", "80"]