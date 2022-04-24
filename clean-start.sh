#!/bin/bash

# setup virtual environment
sudo apt install python3-pip python3-venv -y
python3 -m venv env
source ./env/bin/activate

# install dependencies
pip3 install -r requirements.txt

# run bootstrapper
python3 main.py

# deactivate virtual environment
deactivate
