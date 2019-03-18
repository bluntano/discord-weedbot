# This is the Python bot.

import os
import time

# for random value from 1 to 100 (look below in the @client.command)

from random import *

# Taking token and other stuff from .env file

import dotenv
from os.path import join, dirname
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env"))
os.environ.update(dotenv)

TOKEN = os.environ.get("TOKEN") # Thats a discord bot token from that .env file

# Now it's time to import discord and do the weed stuff

import discord
print(discord.__version__) # should print out (0.16.12)
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
client = Bot(command_prefix = ["w", "W"])
speed=0.01 # how fast will it edit the message

@client.event
async def on_ready():
    print("Weed is ready to serve!") # when its ready

# So this client event below is for command cooldown
# to show how much time left till you can use the command again
    
@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(ctx.message.channel, content='Fuck off cunt!!! This command is on a **%.2f**s cooldown' % error.retry_after)
    raise error  # re-raise the error so all the errors will still show up in console

@client.command(pass_context=True)
@commands.cooldown(1, 20, commands.BucketType.server) # on this, weed command cooldown has set to 20 seconds
async def eed(ctx): # lol eed
    msg=await client.send_message(ctx.message.channel, "Starting to smoke")
    msgWait=time.sleep(3)
    msg1=await client.edit_message(msg, "🚬")
    msgWait2=time.sleep(speed)
    msg2=await client.edit_message(msg1, "🚬☁")
    msgWait3=time.sleep(speed)
    msg3=await client.edit_message(msg2, "🚬☁☁")
    msgWait4=time.sleep(speed)
    msg4=await client.edit_message(msg3, "🚬☁☁☁")
    msgWait5=time.sleep(5)
    msg5=await client.edit_message(msg4, "🚬☁☁☁")
    msgWait6=time.sleep(speed)
    msg6=await client.edit_message(msg5, "🚬☁☁")
    msgWait7=time.sleep(speed)
    msg7=await client.edit_message(msg6, "🚬☁")
    msgWait8=time.sleep(speed)
    msg8=await client.edit_message(msg7, "🚬")
    x = randint(1, 100)    # Pick a random number between 1 and 100.
    #print (x)
    msgWait9=time.sleep(speed)
    msg9=await client.edit_message(msg8, "You are {}% high, my dude!".format(x))
    
    # ".format(x)" is what variable will it use inside the curly brackets.

    # also thank you, CroeyStoey, for suggesting idea of bot telling you how high are you.
    # check him out on Twitter if you want @croeystoey!

    #theEnd=time.sleep(1)
    #msgDelet=await client.delete_message(msg9)

client.run(TOKEN)  # Where 'TOKEN' is your bot token