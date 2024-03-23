FROM ubuntu:24.04

WORKDIR /usr/scripts/

RUN mkdir -p /usr/backup/

COPY . .

RUN chmod +x clean-backup.sh

CMD ["tail", "-f", "/dev/null"]