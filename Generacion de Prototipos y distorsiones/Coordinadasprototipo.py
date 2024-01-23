# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:27:07 2022

@author: UdeSA
"""

"""
Codigo para conocer las posiciones X,Y de los pixeles pintados de rojo en el prototipo L0
"""

import cv2
import numpy as np

from PIL import Image
 
 
im = cv2.imread("L0.png")
with np.printoptions(threshold=np.inf):
    print(im)
red=[255, 0, 0]

Y, X = np.where(np.all(im==red,axis=2))

print(X,Y)

zipped = np.column_stack((X,Y))
print(len(zipped))

print(zipped)

np.savetxt("coordinadasL0.csv", zipped, delimiter=",")



from PIL import Image

im = Image.open('L0.png') # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
print (pix)  # Get the RGBA Value of the a pixel of an image
