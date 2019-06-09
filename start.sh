#!/bin/bash

# This script is executed by server.js: it basically powers up the weed smoker bot.
# It also has a pip command that is required to execute before launching the bot.
# Otherwise the bot won't start up.

# Display Python code logs (Errors, printings, etc.)
export PYTHONUNBUFFERED=true

# Make sure you have Python 3.5 installed (e.g. 3.5.2)
pythonversion=$(python3 --version)
vernum="3.5.2"

if [[ $pythonversion =~ $vernum ]];
then
	python3 -m pip install --upgrade pip --user

	# Install the requirements
	# Uncomment the command below to install from the requirements file
	cd weedbot
	pip3 install -r req.txt --user

	# Finally, start the bot
	python3 WeedBot.py
else
	echo "Failed to run :("
fi
