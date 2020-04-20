# This is the Python bot.
# Licensed under MIT license
# Copyright (c) 2019 Bluntano
import os
import glob
import json
from random import *
from random import choice
from PickerNUploader import PickerAndUploader, NoFilesInDropboxError
from threading import Thread
from Config import *

# Now it's time to import discord and do the weed stuff
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
pau = PickerAndUploader()
client = Bot(command_prefix = ["w", "W"])
speed = 0.10 # how fast will it edit the message

def bot_id():
    return client.user.id

# when its ready
@client.event
async def on_ready():
    pau.create_folder()
    game = discord.Game("Weed time!")
    await client.change_presence(activity=game)
    print("Weed is ready to serve!")

# when joined new server
@client.event
async def on_guild_join(guild):
    channel = discord.utils.get(guild.channels, name="weedpics")
    if not channel:
        await guild.create_text_channel('weedpics')

# Error handling
@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        return
    elif isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CommandError):
        raise error

# Looks for them weed pictures in particular text channel
@client.event
async def on_message(message):

    # Allow 'weed'/'Weed' or other commands in general to work
    await client.process_commands(message)

    # If message author is bot or the bot itselt, ignore.
    if message.author.bot or message.author.id == client.user.id: return

    # If the message doesn't have attachments
    if message.attachments == []: return

    # Look for channel by name '#weedpic-requests'
    channel = discord.utils.get(message.guild.channels, name='weedpics')

    # If it's not the weedpic-requests channel
    if message.channel != channel: return

    # Take the link, and start the upload process
    link = message.attachments[0].url
    await message.delete()
    msg = await message.channel.send("⏳ Uploading")
    try:
        pau.upload_picture_to_dropbox(url=link)
        await msg.edit(content="✅ Uploaded!", delete_after=5)
    except Exception as err:
        await msg.edit(content=f"❌ Failed to upload:\n||`{str(err)}`||", delete_after=5)
        raise commands.CommandError(f"Failed to upload: {str(err)}")

# The juicy stuff here (command event)
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.guild)
async def eed(ctx): # lol eed

    # Starting to smoke!!!! 420 blaze it!!! (Edits one message 9 times)
    msg = await ctx.send("Starting to smoke")
    await asyncio.sleep(1)
    await msg.edit(content="🚬")
    await asyncio.sleep(speed)
    await msg.edit(content="🚬☁")
    await asyncio.sleep(speed)
    await msg.edit(content="🚬☁☁")
    await asyncio.sleep(speed)
    await msg.edit(content="🚬☁☁☁")
    await asyncio.sleep(5)
    await msg.edit(content="🚬☁☁☁")
    await asyncio.sleep(speed)
    await msg.edit(content="🚬☁☁")
    await asyncio.sleep(speed)
    await msg.edit(content="🚬☁")
    await asyncio.sleep(speed)
    await msg.edit(content="🚬")
    await asyncio.sleep(speed)
    await msg.delete()

    # Picks a random number between 0 and 100.
    x = randint(0, 100)

    # User tag
    usertag = str(ctx.message.author.id)

    # Custom weed messages
    #twentyfive_set, fifty_set, seventyfive_set, onehundred_set = []
    with open('sentences.json') as f:
        data = json.load(f)
        twentyfive_set = data['twentyfive_set']
        fifty_set = data['fifty_set']
        seventyfive_set = data['seventyfive_set']
        onehundred_set = data['onehundred_set']
    
    try:
        picture = pau.pick_random_picture()
    except NoFilesInDropboxError:
        pass

    for file in glob.glob("picture.*"):
        msgcontent = ""
        if x <= 25: msgcontent = choice(twentyfive_set)
        elif x <= 50: msgcontent = choice(fifty_set)
        elif x <= 75: msgcontent = choice(seventyfive_set)
        elif x <= 100: msgcontent = choice(onehundred_set)
        file_to_send = discord.File(fp=file, filename=f"smok_weed_evryday.{file.rsplit('.', 1)[1]}", spoiler=True)
        await ctx.send(file=file_to_send, content=f"<@{usertag}> {msgcontent.format(x)}")

async def run():
    await client.start(DISCORD_TOKEN)  # Where 'TOKEN' is your bot token

def run_it_forever(loop):
    loop.run_forever()

def bot_alive():
    loop = asyncio.get_event_loop()
    loop.create_task(run())

    t = Thread(target=run_it_forever, args=(loop,))
    t.start()