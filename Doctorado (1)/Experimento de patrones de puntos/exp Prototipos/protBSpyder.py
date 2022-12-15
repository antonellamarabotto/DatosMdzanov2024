# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:28:18 2021

@author: Antonella
"""


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

#Info Participante
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


"""
Funcion que crea al prototipo
"""
def prototipos(width, height):
        
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
   # print(img[randwidth[1],randheight[1],:])
    img = array(img)
    return img
#    return randwidth
#    return randheight
    
#width=300
#height=300
prototipo=prototipos(width, height)


stimulus = visual.ImageStim(win=win, image=prototipo, mask=None, pos=(0,0), size=(width,height) ,colorSpace='rgb')
stimulus.draw()
win.flip()
core.wait(5)


"""
Funciones que producen las distorsiones L1, L2, L3, L4, L5 y L7

"""

# puntos=prototipos(width, height)
# def L2(puntos, A1, A2, A3, A4, A5):
#     Areas=[A1,A2,A3,A4,A5]
#     positions=[]
#     for i in range (0,len(puntos)):
#         Area=random.choices(Areas, weights=(75,15,5,3,2), *, cum_weights=None, k=1)
#         if Area=="A1":
#             positions.append(A1(puntos[i][0],puntos[i][1]))
#         elif Area=="A2":
#             positions.append(A1(puntos[i][0],puntos[i][1]))
#         elif Area=="A3":
#             positions.append(A1(puntos[i][0],puntos[i][1]))
#         elif Area=="A4":
#             positions.append(A1(puntos[i][0],puntos[i][1]))
#         elif Area=="A5":
#             positions.append(A1(puntos[i][0],puntos[i][1]))



# """
# Las siguientes funciones me dan una posicion dentro de las areas 1, 2, 3, 4 y 5
# """
# #A1: Area 1, el punto se queda en su posicion inicial
# def A1(randwidth, randheight):
#     posicionA1=[randwidth, randheight]
#     return posicionA1
    
# #A2: Area 2, el punto se mueve a una de las 8 posiciones al rededor de su posicion inicial
# def A2(randwidth, randheight):
#     AreaL2=[]
#     for i in range (-1,2):
#         for j in range (-1,2):
#             if i!=0 or j!=0:
#                 AreaL2.append([randwidth+i, randheight+j])
#             else:
#                 continue
#     indiceA2= np.random.randint(0, 9)
#     posicionA2=AreaL2[indiceA2]
#     return posicionA2

# #A3: Area 3, el punto se mueve a una de las 16 posiciones al rededor del area 2 y 1.
# def A3(randwidth, randheight):
#     AreaL3=[]
#     for i in range (-2,3):
#         for j in range (-2,3):
#             if i==2 or j==2 or i==-2 or j==-2:
#                 AreaL3.append([randwidth+i, randheight+j])
#             else:
#                 continue
#     indiceA3= np.random.randint(0, 17)
#     posicionA3=AreaL3[indiceA3]
#     return posicionA3
