#!/bin/bash

# This script is executed by server.js: it basically powers up the weed smoker bot.
# It also has a pip command that is required to execute before launching the bot.
# Otherwise the bot won't start up.

# Quick note: Shell scripts do not work on Windows so, I would suggest executing
# directly with python3 command.

pip3 --version

# Make sure you have Python 3.5 installed (e.g. 3.5.2)

python3 --version

#python3 -m pip install --upgrade pip --user

# Install the requirements
# Uncomment the command below to install from the requirements file

#python3 -m pip install -r ./weedbot/req.txt --user

# Finally, start the bot

python3 ./weedbot/weed.py