FROM python:3.11.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/scripts/

RUN mkdir -p /usr/backup/

COPY . .

RUN chmod +x clean-backup.sh