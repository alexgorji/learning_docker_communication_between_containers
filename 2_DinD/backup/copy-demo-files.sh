#!/bin/bash

echo "backup copy-demo-files.sh"
echo "Running copy script of demo-1"

echo "Running copy script of demo-1"
docker exec dind-demo-1 sh ./copy-to-backup.sh
echo "Running copy script of demo-2"
docker exec dind-demo-2 sh ./copy-to-backup.sh
echo "backup done."