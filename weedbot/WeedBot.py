# This is the Python bot.
# Licensed under MIT license
# Copyright (c) 2019 Bluntano
import os
import glob

from random import *
from random import choice

from dotenv import load_dotenv
load_dotenv(verbose=True)

# Discord Bot token
TOKEN = os.getenv("DISCORD")

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
    await client.change_presence(game=discord.Game(name='some weed m8'))
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
                import FilePickerAndUploader as FPaU
                FPaU.Tools.upload_picture_to_dropbox(url=link)
                status = FPaU.Tools.upload_picture_to_dropbox.is_uploaded
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
                    elif status == "FileTooBig":
                        await client.edit_message(msg_status, "❌ Failed to upload: Video file size is bigger than 3.3 MB!")
                        break
                    elif status == "DimensionsTooSmall":
                        await client.edit_message(msg_status, "❌ Failed to upload: Video dimensions are too small!")
                        break

# The juicy stuff here (command event)
@client.command(pass_context=True)
@commands.cooldown(1, 12, commands.BucketType.server) # on this, weed command cooldown has set to 18 seconds
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

    # Custom messages
    twentyfive_set = [
        "Oh wow! Just {}% high? Man, you love no weed I see :/",
        "That sucks! {}% on weed... try better next time",
        "You didn't smoke at all! Only {}% high huh. We gave you the blunt for a reason smh",
        "FUCKIN' SMOKE IT PROPERLY, WE ABT TO GET HIGH, NOT TO STAY SOBER!!1! {}% high >:/",
        "You're not a weeder :c, you're only just {}% high... #disrespecc"
    ]

    fifty_set = [
        "Nice blunt you got there! {}% high",
        "Make sure you'll go all the way to a hundred. Good job! {}% high",
        "You can be higher than {}%, come on, dude! :D",
        "...did Seth give you that rolled weed? No wonder you're {}% high",
        "You can do it! COME OOOON!!! {}%"
    ]

    seventyfive_set = [
        "SMOK WED EVRIDAY!!! {}%",
        "NICEEEEEEEE!!! {}%",
        "All the way to 100 from {}%, babyyyyyyyyyy!!!",
        "You know well how to smoke some good-ass grass! Your {}% highness explains it well ;)",
        "Your middle name must be Weed because, holy shit! That blunt hit got you {}% high, man :D"
    ]

    hundred_set = [
        "WOOOWW YOU ARE HIIIIIGHHHH!!! {}%",
        "Seth is gay, keep smoking dank-ass weed ;3 get higher than {}%",
        "WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOAH {}% High",
        "You're a weed legend, my dude! {}% highness is not baaaaad!!!",
        "WELCOME TO THE WEED CLUB BABYYYYYYYY!!!! {}% high!"
    ]

    # Last message being edited
    msgWait9=asyncio.sleep(speed)
    msgDelete = await client.delete_message(msg8)

    # Dropbox File Picker/Random Picture Picker
    import FilePickerAndUploader as FPaU
    picture = FPaU.Tools.pick_random_picture()

    # Looks for the picture file that just got downloaded with file picker
    # With either .png or .jpg extension, depending on the picture downloaded
    asyncio.sleep(5)
    for file in glob.glob("picture.*"):
        if x <= 25:
            msgcontent = choice(twentyfive_set)
            msgPicture=await client.send_file(ctx.message.channel, "./" + file, content="<@" + usertag + "> " + msgcontent.format(x))
        elif x <= 50:
            msgcontent = choice(fifty_set)
            msgPicture=await client.send_file(ctx.message.channel, "./" + file, content="<@" + usertag + "> " + msgcontent.format(x))
        elif x <= 75:
            msgcontent = choice(seventyfive_set)
            msgPicture=await client.send_file(ctx.message.channel, "./" + file, content="<@" + usertag + "> " + msgcontent.format(x))
        elif x <= 100:
            msgcontent = choice(hundred_set)
            msgPicture=await client.send_file(ctx.message.channel, "./" + file, content="<@" + usertag + "> " + msgcontent.format(x))

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