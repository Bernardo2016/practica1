#!/bin/bash
cd /home/ec2-user/ejercicio4
python3 procesar.py
pkill -f "python3 -m http.server 8080"
nohup python3 -m http.server 8080 > /dev/null 2>&1 &
