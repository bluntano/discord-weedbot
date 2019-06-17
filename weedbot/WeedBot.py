# This is the Python bot.
# Licensed under MIT license
# Copyright (c) 2019 Bluntano
import os
import glob

from random import *

# Taking token and other stuff from .env file
import json
file = open('token.json')
content = json.load(file)

# Discord Bot token
TOKEN = content['discord_token']

# Now it's time to import discord and do the weed stuff
import discord
#print(discord.__version__) # should print out (0.16.12)
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
client = Bot(command_prefix = ["w", "W"])
speed=0.1 # how fast will it edit the message

# when its ready
@client.event
async def on_ready():
    print("Weed is ready to serve!")

# Error handling
@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        return
    elif isinstance(error, commands.CommandNotFound):
        return
    raise error  # re-raise the error so all the errors will still show up in console

# Looks for them weed pictures in particular text channel
@client.event
async def on_message(message):

    # Allow 'weed'/'Weed' or other commands in general to work
    await client.process_commands(message) 

    # If message author is bot or the bot itselt, ignore.
    if message.author == client.user:
        return
    elif message.author.bot == True:
        return
    else:
        # Look for channel by name '#weedpic-requests'
        channel = discord.utils.get(message.server.channels, name='weedpic-requests', type=discord.ChannelType.text)

        # If it's not the weedpic-requests channel
        if message.channel != channel:
            return
        else:
            # If the message doesn't have attachments
            if message.attachments == []:
                return
            else:
                # Take the link, and start the upload process
                link = message.attachments[0]['url']
                import DropboxFileUploader
                DropboxFileUploader.upload_picture_to_dropbox(url=link)
                status = DropboxFileUploader.upload_picture_to_dropbox.is_uploaded
                while True:
                    msg_status = await client.send_message(message.channel, "⏳ Uploading")
                    if status == True:
                        await client.edit_message(msg_status, "✅ Uploaded!")
                        break
                    elif status == False:
                        await client.edit_message(msg_status, "❌ There was a problem uploading the picture. Please try again later!")
                        break
                    elif status == None:
                        await client.edit_message(msg_status, "❌ Unknown / Unsupported file extension!")
                        break

# The juicy stuff here (command event)
@client.command(pass_context=True)
@commands.cooldown(1, 18, commands.BucketType.server) # on this, weed command cooldown has set to 18 seconds
async def eed(ctx): # lol eed

    # Starting to smoke!!!! 420 blaze it!!! (Edits one message 9 times)
    msg=await client.send_message(ctx.message.channel, "Starting to smoke")
    await asyncio.sleep(1)
    msg1=await client.edit_message(msg, "🚬")
    msgWait2=asyncio.sleep(speed)
    msg2=await client.edit_message(msg1, "🚬☁")
    msgWait3=asyncio.sleep(speed)
    msg3=await client.edit_message(msg2, "🚬☁☁")
    msgWait4=asyncio.sleep(speed)
    msg4=await client.edit_message(msg3, "🚬☁☁☁")
    msgWait5=asyncio.sleep(5)
    msg5=await client.edit_message(msg4, "🚬☁☁☁")
    msgWait6=asyncio.sleep(speed)
    msg6=await client.edit_message(msg5, "🚬☁☁")
    msgWait7=asyncio.sleep(speed)
    msg7=await client.edit_message(msg6, "🚬☁")
    msgWait8=asyncio.sleep(speed)
    msg8=await client.edit_message(msg7, "🚬")

    # Picks a random number between 0 and 100.
    x = randint(0, 100)

    # User tag
    user = ctx.message.author.id
    usertag = str(user)

    # Last message being edited
    msgWait9=asyncio.sleep(speed)
    #msg9=await client.edit_message(msg8, "<@" + usertag + "> You are {}% high, my dude!".format(x))
    msgDelete = await client.delete_message(msg8)

    # Dropbox File Picker/Random Picture Picker
    # I needed a better, more convenient way to store these anime/non-anime blunt pictures, my boi
    import DropboxFilePicker
    picture = DropboxFilePicker.RandomPicture()

    # Looks for the picture file that just got downloaded with file picker
    # With either .png or .jpg extension, depending on the picture downloaded
    for file in glob.glob("*.png") or glob.glob("*.jpg") or glob.glob("*.gif"):
        msgPicture=await client.send_file(ctx.message.channel, "./" + file, content="<@" + usertag + "> You are {}% high, my dude!".format(x))

    if x > 50: # if the x value is higher than 50

        # Gathers the command autor and the voice channel
        user = ctx.message.author
        voice_channel = user.voice.voice_channel
        channel = None
        if voice_channel != None:

            # Takes user's voice channel where he joined
            channel=voice_channel.name

            # Streaming 'weed.mp3' file
            vc = await client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('weed.mp3')
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)

            # Disconnects when it's done playing
            player.stop()
            await vc.disconnect()

client.run(TOKEN)  # Where 'TOKEN' is your bot token