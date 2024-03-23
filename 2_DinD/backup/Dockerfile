FROM docker

WORKDIR /usr/scripts/

RUN mkdir -p /usr/backup/

COPY . .

RUN chmod +x clean-backup.sh
RUN chmod +x copy-demo-files.sh

CMD ["tail", "-f", "/dev/null"]