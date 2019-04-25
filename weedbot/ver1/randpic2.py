import os

# Reads the folder's content
path = r"./pic/"

# Important stuff to make random choice to work
from random import choice
from scipy import *

# Randpic v2.0 (made quickly lol)
def pickRand():

    # Picks a random file from the set path
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    folder = "./pic/"
    filename = folder + random_filename
    return filename