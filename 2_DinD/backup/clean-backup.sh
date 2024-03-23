#!/bin/bash

echo "backup: Removing contents of backup."
cd /usr/backup
rm -rf ./*
echo "backup: Contents removed from backup."

