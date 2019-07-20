#!/bin/bash

# This script is executed by server.js: it basically powers up the weed smoker bot.
# It also has a pip command that is required to execute before launching the bot.
# Otherwise the bot won't start up.

# portable MediaInfo library for Linux (otherwise is taken from the system library folder instead)
export LD_LIBRARY_PATH=~/weedbot/mediainfo/

# Make sure you have Python 3.5 installed (e.g. 3.5.2)
pythonversion=$(python3 --version)
echo $pythonversion

if [[ $pythonversion =~ "3.5.2" ]];
then
  # Display Python code logs (Errors, printings, etc.)
  export PYTHONUNBUFFERED=true
  
	python3 -m pip install --upgrade pip --user

	# Install the requirements
	# Uncomment the command below to install from the requirements file
	cd weedbot
	pip3 install -r req.txt --user

	# Finally, start the bot
	python3 WeedBot.py
else
	echo "Failed to run :( Either, Python is not installed or, it is incorrect version."
fi
