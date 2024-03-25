FROM python:3.11.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/data/

RUN mkdir -p /usr/backup/

COPY . .

RUN chmod +x copy-to-backup.sh

CMD [ "python3", "/usr/data/ipc-server.py" ]
