####################################################################################################
# Script that uploads pictures from Discord chat to Dropbox
# How it works?
# --------------------------------------------------------------------------------------------------
# 1. The function gets called with link provided
# 2. Dropbox gets also initiated, counts up the files currently in the cloud storage
# 3. Downloads the picture from Discord attachments server, renames it to
#    <total file count on Dropbox + 1>.png/jpg
# 4. Stores it on the server before uploading
# 5. Takes just downloaded and renamed picture and starts uploading it to '/weed_pictures' folder on
#    Dropbox
# --------------------------------------------------------------------------------------------------
# It currently works as in like, one by one. Hopefully Discord users won't get ape-shit because,
# the function might just stop working after massive amount of loads applied to it. I'll think of
# something essentially, if that happends.
# ==================================================================================================
# Licensed under MIT license
# Copyright (c) 2019 Bluntano
# ==================================================================================================
import os
import dropbox

import requests

# Taking token and other stuff from token.json file
import json
tokens = open('token.json')
content = json.load(tokens)

# Dropbox app token, taken from the json file
token = content['dbx_token']

# Activating Dropbox and path from where to take pictures
dbx = dropbox.Dropbox(token)
WeedPictures = '/weed_pictures'

def upload_picture_to_dropbox(url):
    '''Downloads picture from given URL and stores it onto the server.'''

    # File extensions
    png = 'png'
    jpg = 'jpg'

    # If the link ends with with either .png or .jpg file extension
    if url.endswith(png):
        extension = '.png'
    elif url.endswith(jpg):
        extension = '.jpg'
    else:
        return

    # Counts up files in a folder (IMPORTANT!!!)
    so_meta = dbx.files_list_folder(WeedPictures).entries
    fname = []
    for i in so_meta:
        fname.append(i)

    # Files in total
    FileCount = len(fname)
    x = FileCount + 1
    #print('{}'.format(x))

    # Make a folder called 'upload-pictures' if it doesn't already exist
    while not os.path.exists('./upload-pictures/'):
        print("===========================================")
        print("Making directory for new received pictures")
        os.mkdir('./upload-pictures/')

    # Download picture from Discord attachments server
    # (Keep in mind, urllib or wget does not work, it is one protected server)
    # (Returns with HTTPError number 403: Forbidden)
    headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
    }
    r = requests.get(url=url, headers=headers, stream=True)
    with open('./upload-pictures/' + str(x) + extension, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    # Read the just downloaded picture and upload it to Dropbox
    with open('./upload-pictures/' + str(x) + extension, 'rb') as f:
        print("===========================================")
        print("Uploading picture to Dropbox")
        try:
            dbx.files_upload(f.read(), '/weed_pictures/' + str(x) + extension, mute=True)
            print("Done!")
        except Exception as e:
            print("Error occured:", e)

# For testing purposes, uncomment function call below this comment.
#upload_picture_to_dropbox()