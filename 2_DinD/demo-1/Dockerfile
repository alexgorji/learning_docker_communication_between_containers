FROM ubuntu:24.04

WORKDIR /usr/data/

RUN mkdir -p /usr/backup/

COPY . .

RUN chmod +x copy-to-backup.sh

CMD ["tail", "-f", "/dev/null"]