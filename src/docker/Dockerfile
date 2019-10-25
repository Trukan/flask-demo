FROM python:3.7-slim

WORKDIR /app

ADD ..../.. /app

RUN pip3 --no-cache-dir install -r requirements.txt

RUN chmod +x src/docker/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./src/docker/entrypoint.sh"]