#!/bin/bash

echo "demo-1: copying started."
sleep 2
cp -r /usr/data/demo-data-1/demo_1 /usr/backup
cp -r /usr/data/demo-data-1/demo_1_a.txt /usr/backup
cp -r /usr/data/demo-data-1/demo_1_b.txt /usr/backup
echo "demo-1: copying finished."