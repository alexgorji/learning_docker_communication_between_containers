backup can communicate with demo-1 and demo-2 over http protocol and invoke copying files.

`docker compose up -d --build`

`docker compose exec backup sh ./clean-backup.sh `

`docker compose exec backup sh ./copy-demo-files.sh `

