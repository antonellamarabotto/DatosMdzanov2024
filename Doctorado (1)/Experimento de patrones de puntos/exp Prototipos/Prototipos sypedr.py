# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:20:11 2021

@author: Antonella
"""
import random
from PIL import Image
import numpy as np

width = 1300
height = 700

# Make empty black image of size (100,100)
img = np.zeros((width, height, 3), np.uint8)

red = [255,0,0]

# Change pixel (50,50) to red
img[650,350] = red

red = [255,0,0]

#Lists of 9 random widths and heights
randwidth=np.random.randint(0,1300,(9))
randheight=np.random.randint(0,700,(9))
print(randwidth)
print(randwidth[0])
for i in range (0, len(randwidth)):
    img[randwidth[i],randheight[i]]=red
    red = [255,0,0]

im = Image.fromarray(img, 'RGB')
im.show()