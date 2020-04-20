####################################################################################################
# Script that uploads pictures from Discord chat to Dropbox, and picks pictures when the function is
# triggered in any way possible.
# --------------------------------------------------------------------------------------------------
# Uploader - How it works?
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
from dropbox.exceptions import ApiError
from random import *
import glob
from Config import DROPBOX_TOKEN

# urllib - for downloading the picture from temp link
import urllib.request
import requests

# For video file extension
from pymediainfo import MediaInfo

# Activating Dropbox and path from where to take pictures
dbx = dropbox.Dropbox(DROPBOX_TOKEN)

class PickerAndUploader:
    '''Stuff for uploading onto and picking from Dropbox cloud storage'''

    def __init__(self):
        '''Picker and uploader (from and to dropbox respectively)'''
        self.supported_types = ['png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'webm']
        self.upload_media = './upload-media/'
        self.filesize_limit = 7200000
        self.dropbox_path = '/weedbot-media/' # I set my Dropbox token to access one particular folder only
    
    def download_from_discord(self, url: str):
        '''Downloads picture before it deletes from Discord
        Parameters
        ----------
        url: str
            URL to download onto the server.
        '''
        self.url = url
        url_lowered = self.url.lower()
        url_ext = url_lowered.rsplit('.', 1)[1]

        # Supported extensions
        if url_ext not in self.supported_types:
            raise NotVideoOrPhotoError("Not supported video or photo file.")

        # Counts up files in a folder (IMPORTANT!!!)
        meta_stuff = dbx.files_list_folder(self.dropbox_path).entries
        entries = []
        for i in meta_stuff:
            entries.append(i)

        # Files in total
        FileCount = len(entries)
        new_file = FileCount + 1
	
	    # The upload path variable for better... code, idk
        self.new_file_path = f'{str(new_file)}.{url_ext}'
        self.upload_path = f'{self.upload_media}{self.new_file_path}'

        # Make a folder called 'upload-media' if it doesn't already exist
        while not os.path.exists(self.upload_media):
            print("== Making directory for new received pictures ==")
            os.mkdir(self.upload_media)

        # Download picture from Discord attachments server
        headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
        }
        r = requests.get(url=url, headers=headers, stream=True)
        with open(self.upload_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        
        # MediaInfo library
        # Checks file size of submitted picture or video, also checks video dimensions
        # On Linux host, LD_LIBRARY_PATH on start.sh file has defined the location
        # of the library files
        media_info = MediaInfo.parse(self.upload_path)
        t = media_info.tracks[0]
        filesize = t.to_data()["file_size"]
        if filesize > self.filesize_limit:
            os.remove(self.upload_path)
            raise FileTooBigError(f"File is bigger than {filesize / 1000000} MB.")

        for track in media_info.tracks:
            if track.track_type == 'Video':
                width = track.width
                height = track.height
                if width < 100 or height < 75:
                    os.remove(self.upload_path)
                    raise VideoDimensionsError("Video dimensions are too small.")

    def create_folder(self):
        '''Creates folder neccessary for storing media files'''
        try:
            dbx.files_create_folder(f'{self.dropbox_path[:-1]}')
        except ApiError:
            print(f"== Folder {self.dropbox_path} already exists. ==")
            pass

    def upload_to_dropbox(self):
        '''Uploads new downloaded file to Dropbox storage'''

        # Read the just downloaded picture and upload it to Dropbox
        with open(self.upload_path, 'rb') as f:
            print(f"== Uploading to Dropbox: {self.upload_path} ==")
            try:
                return dbx.files_upload(f.read(), f'{self.dropbox_path}{self.new_file_path}', mute=True)
            except Exception as e:
                raise UploadingError(e)

    def pick_random_picture(self):
        '''Picks a completely random picture or video from Dropbox storage'''

        print("== Picker initiated! Please wait... ==")

        # Counts up files in a folder (IMPORTANT!!!)
        meta_stuff = dbx.files_list_folder(self.dropbox_path).entries
        entries = []
        for i in meta_stuff:
            entries.append(i)
        
        try:
            # A random digit between 1 and number of files in total
            file_count = len(entries)
            x = randint(1, file_count)
            print(f"== Media files in total: {file_count} ==")
            searchpicture = dbx.files_search(self.dropbox_path[:-1], f'{x}').matches[0].metadata.name
        except Exception as err:
            print("Fuck!", err)
            raise NoFilesInDropboxError

        file_result = str(searchpicture)
        print(f"Randomly picked file: {file_result}")

        # Takes file extension from the picked picture
        file_ext = file_result.split('.')[1]
        #print(FileExtension)

        # Takes the file name and gets a temporary link for the image
        url = dbx.files_get_temporary_link(path=f'{self.dropbox_path}{file_result}').link
        file_url = str(url)

        # Checks the picture file, removes the picture which was previously
        # downloaded if it exists
        picture_with_ext = f'picture.{file_ext}'
        for pic_file in glob.glob('picture.*'):
            if os.path.exists(pic_file): os.remove(pic_file)
            elif os.path.exist(picture_with_ext): os.remove(picture_with_ext)
            else: print("== Picture does not exist! Downloading one... ==")

        download_picture = urllib.request.urlretrieve(url=file_url, filename=f'./{picture_with_ext}')
        return True

class NotVideoOrPhotoError(Exception):
    """raised when submitted file is not picture or video file"""
    pass

class FileTooBigError(Exception):
    """raised when file exceeds the size limit"""
    pass

class VideoDimensionsError(Exception):
    """raised when there's something up with video dimensions"""
    pass

class UploadingError(Exception):
    """raised when uploading error occured"""
    pass

class NoFilesInDropboxError(Exception):
    """raised on rare occasions: when no pictures to pick from Dropbox file storage"""
    pass