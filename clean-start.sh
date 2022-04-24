#!/bin/sh

# setup virtual environment
sudo apt install python3-venv -y
python3 -m venv env

# install dependencies
./env/bin/pip install -r requirements.txt

# run bootstrapper
clear && ./env/bin/python3 main.py
