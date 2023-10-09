# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:41:35 2023

@author: haris
"""

# This program is a Nerves of steel timer

import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images
import random # the random linrary allows us to select a random variable

# importing the closing image
im = Image.open("times-up.jpeg")
# importing the opening image
ip = Image.open("Stand-up.jpg")
# display the opening image
ip.show()

# inform the users the game has started
print("Players Stand")

# assign a random variable between 5 and 25
a = random.randint(5,25)


# set a timer with the random variable
set_time = int(a)
time.sleep(set_time)

# display the closing image
im.show()
# inform users tume is up
print("times up! Last to sit down Wins!!!!!!")
