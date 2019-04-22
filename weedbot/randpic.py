# Random Picture Picker
import os

# Those are very needed
from random import choice
from scipy import *

# List of pictures in the 'bb' directory
picture_set = [
    './bb/1.jpg',
    './bb/2.jpg',
    './bb/3.jpg',
    './bb/4.jpg',
    './bb/5.png',
    './bb/6.png',
    './bb/7.jpg',
    './bb/8.jpg',
    './bb/9.jpg',
    './bb/10.png'
    ]

# Function where it takes a one random choice from the list
def randomPic():
    a = random.choice(picture_set, replace=True)
    return a