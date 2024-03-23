FROM python:3.11.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/data/

RUN mkdir -p /usr/backup/

COPY . .

RUN chmod +x copy-to-backup.sh
