import os

from random import choice
from scipy import *

picture_set = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']

def randomPic():
    a = random.choice(picture_set, replace=True)
    return a