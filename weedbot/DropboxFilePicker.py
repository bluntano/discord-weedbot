# =====================================================
# Licensed under MIT license
# Copyright (c) 2019 Bluntano
# =====================================================
# Script which picks a random picks from Dropbox cloud
import os
import dropbox

from random import *
import glob

from dotenv import load_dotenv
load_dotenv(verbose=True)

# Dropbox app token, taken from the json file
token = os.getenv("DROPBOX")

# urllib - for downloading the picture from temp link
import urllib.request

# Activating Dropbox and path from where to take pictures
dbx = dropbox.Dropbox(token)
WeedPictures = '/weed_pictures/'

# Random Picture function
def RandomPicture():

    print("File Picker initiated! Please wait...")
    print("===========================================")

    # Counts up files in a folder (IMPORTANT!!!)
    so_meta = dbx.files_list_folder(WeedPictures).entries
    fname = []
    for i in so_meta:
        fname.append(i)

    # A random digit between 1 and number of files in total
    FileCount = len(fname)
    y = FileCount
    x = randint(1, y)
    print("Pictures in total:", FileCount)

    # After a generated number, it will search for the picture with the name of that generated number
    # Files are numberized in the storage
    """
    e.g.:
    Random number: 5
    Randomly picked file: 5.png
    """
    searchpicture = dbx.files_search(WeedPictures, '{}'.format(x)).matches[0].metadata.name
    FileResult = str(searchpicture)
    print("Randomly picked file:", FileResult)
    print("===========================================")

    # Takes file extension from the picked picture
    FileExtension = FileResult.split(".")[1]
    #print(FileExtension)

    # Takes the file name and gets a temporary link for the image
    URL = dbx.files_get_temporary_link(path=WeedPictures + FileResult).link
    file_url = str(URL)
    #print(file_url)

    # Checks the picture file, removes the picture which was previously
    # downloaded if it exists
    for pic_file in glob.glob('picture.*'):
        if os.path.exists(pic_file):
            os.remove(pic_file)
        elif os.path.exist('picture.' + FileExtension):
            os.remove('picture.' + FileExtension)
        else:
            print("Picture does not exist! Downloading one...")

    DownloadPic = urllib.request.urlretrieve(url=file_url, filename='./picture' + "." + FileExtension)
    return

# for testing purposes, uncomment the function call below
#RandomPicture()