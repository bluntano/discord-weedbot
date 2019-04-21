import os

from random import choice
from scipy import *

picture_set = ['./bb/1.jpg', './bb/2.jpg', './bb/3.jpg', './bb/4.jpg', './bb/5.png', './bb/6.png', './bb/7.jpg']

def randomPic():
    a = random.choice(picture_set, replace=True)
    return a