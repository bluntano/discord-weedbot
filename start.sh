#!/bin/bash

# Exit early on errors
set -eu

# Delete pictures from previous session
rm -rf upload-media/

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# portable MediaInfo library for Linux (otherwise is taken from the system library folder instead)
export LD_LIBRARY_PATH=~/mediainfo/

pip3 install -r requirements.txt
python3 Server.py
