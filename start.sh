#!/bin/bash

# Exit early on errors
set -eu

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# portable MediaInfo library for Linux (otherwise is taken from the system library folder instead)
export LD_LIBRARY_PATH=~/mediainfo/

# Install Python 3 virtual env
VIRTUALENV=.data/venv

if ! command -v virtualenv; then
  pip3 install virtualenv
fi

if [ ! -d $VIRTUALENV ]; then
  virtualenv -p /usr/bin/python3 $VIRTUALENV
fi

$VIRTUALENV/bin/pip3 install -r requirements.txt
$VIRTUALENV/bin/python3 WeedBot.py
