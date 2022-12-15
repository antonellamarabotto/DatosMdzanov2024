
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, colors, parallel, monitors, prefs
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray, zeros, uint8,array)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import cv2
import matplotlib.pyplot as plt
from psychopy.hardware import keyboard

chequeo = 1
'''
while chequeo == 1:
    
    # Gui for Info
    Informacion_Participante = gui.Dlg(title="Protocol: Prototipos - Paradigm: Prototipos- 2021")
    Informacion_Participante.addText('Subject Information:')
    Informacion_Participante.addField('Code:')
    Informacion_Participante.addField('Examiner:')
    Informacion_Participante.addField('Evaluation Date:(dd/mm/yy)')
    Informacion_Participante.addField('Method:', choices=['None','TMS'])
    Interfaz_Informacion  = Informacion_Participante.show() # Primera estructura a guardar con info de sujeto
    
    ## Info Constrains
    # Cancel Button or empty info
    print(Informacion_Participante.OK)
    if Informacion_Participante.OK == False:
         print('Thanks for Participation')
         core.quit()
    elif not Informacion_Participante.data[0]:
         print('Specify Code')
    elif not Informacion_Participante.data[1]:
         print('Specify Examiner')
    elif not Informacion_Participante.data[2]:
         print('Specify Date')
    else:
        chequeo = 2
'''

## Psychopy3 Window Definition
for mon in monitors.getAllMonitors():
    print(mon, monitors.Monitor(mon).getSizePix())
win = visual.Window(size=(monitors.Monitor(mon).getSizePix()), pos=None, color=('white'), colorSpace='rgb', allowGUI=True ,fullscr=True, monitor='testMonitor', units='pix',winType='pyglet', useFBO=False)
event.Mouse(visible=False)
print(monitors.Monitor(mon).getSizePix())

width  = monitors.Monitor(mon).getSizePix()[0]
height = monitors.Monitor(mon).getSizePix()[1]

# Make empty black image of size (100,100)
img = np.ones((width, height, 3), np.uint8)
red = [255]

#Lists of 9 random widths and heights
randwidth  = np.random.randint(0,width,(9))
randheight = np.random.randint(0,height,(9))

dotImg = []
for i in range(0, 10):
    appendList = []
    for j in range(0,10):
        appendList.append([255,0,0])
    dotImg.append(appendList)

for imgIter in range(0,len(randwidth)):
    img[randwidth[imgIter]-5:randwidth[imgIter]+5,randheight[imgIter]-5:randheight[imgIter]+5] = dotImg
'''
for i in range(0, len(randwidth)):
    for j in range(0,len(randwidth)):
        img[randheight[i]-5:randheight[i]+5,randwidth[j]-5,randwidth[j]+5] = red
'''
print(img[randwidth[1],randheight[1],:])
img = array(img)
stimulus = visual.ImageStim(win=win, image=img, mask=None, pos=(0,0), size=(width,height) ,colorSpace='rgb')

stimulus.draw()
win.flip()

core.wait(5)

