This is a learning project to experiment with different approaches of container communication.

Compose: The host uses docker compose exec to manage the communication.

DinD: One container (backup) uses Docker within Docker principle to use docker exec commands on the other containers (demo-1 and demo-2).

Flask: Two containers (demo-1 and demo-2) use Flask and exposes a port for communicating with it via http protocol. 

Socket: Two containers (demo-1 and demo-2) use server sockets for communication with the other container (backup) which act as a client with a client socket.

The common scenario between experiments:

Three containers `demo-1`, `demo-2`, `backup`

```
├── demo-1
|   ├── demo-data-1
|   |   ├── demo_1
|   |   |   |   └── demo_1_c.txt
|   |   |   ├── demo_1_a.txt
|   |   |   └── demo_1_b.txt
|   ├── copy-to-backup.sh

├── demo-2
|   ├── demo-data-2
|   |   ├── demo_2
|   |   |   └── demo_2_c.txt
|   |   ├── demo_2_a.txt
|   |   └── demo_2_b.txt
|   ├── copy-to-backup.sh

├── backup
|   ├── clean-backup.sh
|   ├── demo-1-copy-to-backup.sh
|   ├── demo-2-copy-to-backup.sh
```
All containers share a backup volume

The copying process will be delayed for 2 seconds in order to simulate possible costly complications.

Each step in script files echos its start and end point.

