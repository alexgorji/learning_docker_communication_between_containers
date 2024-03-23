1. Start all services with: `docker compose up -d`
2. Make copies: `docker compose exec demo-1 ./copy-to-backup.sh` and `docker compose exec demo-2 ./copy-to-backup.sh` 
3. You can clean backup directory with: `docker compose exec backup ./clean-backup.sh`


In this scenario there is no possibility for `backup` to invoke copying inside the two other containers. Only the host can run commands inside all containers.