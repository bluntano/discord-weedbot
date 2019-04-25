# Script which picks a random picks from Dropbox cloud
import os
import dropbox

from random import *

# Taking token and other stuff from .env file
import dotenv
from os.path import join, dirname
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env"))
os.environ.update(dotenv)

# Thats a Dropbox app token from that .env file
DROPBOX_TOKEN = os.environ.get("DBX_TOKEN")

# Activating Dropbox and path from where to take pictures
dbx = dropbox.Dropbox(DROPBOX_TOKEN)
WeedPictures = '/weed_pictures/'

# Random Picture function
def RandomPicture():

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
    print("============================")

    # Takes the file name and gets a temporary link for the image
    # Why temporary link? So that Discord could actually show the picture.
    # It won't show the picture with the regular shared link
    # (Temporary links also have automatic time limit)
    URL = dbx.files_get_temporary_link(path=WeedPictures + FileResult).link
    file_url = str(URL)
    #print(file_url)
    return file_url
