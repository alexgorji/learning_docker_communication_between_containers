#!/bin/bash

echo "backup copy-demo-files.sh"
echo "Running curl to copy script of demo-1"
curl demo-1:5001/copy-files
echo "Running curl to copy script of demo-2"
curl demo-2:5002/copy-files
echo "backup done."