####################################################################################################
# Script that uploads pictures from Discord chat to Dropbox
# How it works?
# --------------------------------------------------------------------------------------------------
# 1. The function gets called with link provided
# 2. Dropbox gets also initiated, counts up the files currently in the cloud storage
# 3. Downloads the picture from Discord attachments server, renames it to
#    <total file count on Dropbox + 1>.png/jpg/whatever file extension supported
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

from dotenv import load_dotenv
load_dotenv(verbose=True)

# Dropbox app token, taken from the json file
token = os.getenv("DROPBOX")

# For video file extension
from pymediainfo import MediaInfo

# Activating Dropbox and path from where to take pictures
dbx = dropbox.Dropbox(token)
WeedPictures = '/weed_pictures'

def upload_picture_to_dropbox(url):
    '''Downloads picture from given URL and stores it onto the server.'''

    # File extensions
    png = ['PNG', 'png', 'Png']
    jpg = ['JPG', 'jpg', 'Jpg']
    gif = ['GIF', 'gif', 'Gif']
    mp4 = ['MP4', 'mp4', 'Mp4']
    mov = ['MOV', 'mov', 'Mov']

    # Supported extensions
    if url.endswith(tuple(png)):
        extension = '.png'
    elif url.endswith(tuple(jpg)):
        extension = '.jpg'
    elif url.endswith(tuple(gif)):
        extension = '.gif'
    elif url.endswith(tuple(mp4)):
        extension = '.mp4'
    elif url.endswith(tuple(mov)):
        extension = '.mov'
    else:
        print("Submitted file is not a picture:", url)
        upload_picture_to_dropbox.is_uploaded = None
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
	
	# The upload path variable for better... code, idk
    upload_path = './upload-pictures/' + str(x) + extension

    # Make a folder called 'upload-pictures' if it doesn't already exist
    while not os.path.exists('./upload-pictures/'):
        print("===========================================")
        print("Making directory for new received pictures")
        os.mkdir('./upload-pictures/')

    # Download picture from Discord attachments server
    headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
    }
    r = requests.get(url=url, headers=headers, stream=True)
    with open(upload_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    # For checking if the file uploaded to the server is mp4 and
    # before uploading it to Dropbox.
    if extension is mp4 or mov:

        # Linux (portable, LD_LIBRARY_PATH set in start.sh)
        media_info = MediaInfo.parse(upload_path, library_file='./mediainfo/libmediainfo.so.0')

        # Windows (high chance Windows has MediaInfo library installed)
        #media_info = MediaInfo.parse(upload_path)

        t = media_info.tracks[0]
        filesize = t.to_data()["file_size"]
        if filesize > 3300000:
            upload_picture_to_dropbox.is_uploaded = "FileTooBig"
            os.remove(upload_path)
            return
        else:
            for track in media_info.tracks:
                if track.track_type == 'Video':
                    width = track.width
                    height = track.height
                    print("Video resolution: {}x{}".format(track.width, track.height))
                    if width < 100 or height < 75:
                        upload_picture_to_dropbox.is_uploaded = "DimensionsTooSmall"
                        os.remove(upload_path)
                        return

    
    # Read the just downloaded picture and upload it to Dropbox
    with open(upload_path, 'rb') as f:
        print("===========================================")
        print("Uploading picture to Dropbox:", url)
        try:
            dbx.files_upload(f.read(), WeedPictures + '/' + str(x) + extension, mute=True)
            upload_picture_to_dropbox.is_uploaded = True
            return print("Done!")
        except Exception as e:
            upload_picture_to_dropbox.is_uploaded = False
            return print("Error occured:", e)

# For testing purposes, uncomment function call below this comment.
#upload_picture_to_dropbox()