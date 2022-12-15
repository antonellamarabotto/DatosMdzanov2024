
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, colors, parallel, monitors, prefs
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray, zeros, uint8,array)
import random
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import cv2
import matplotlib.pyplot as plt
from psychopy.hardware import keyboard
import copy

import math
from PIL import Image, ImageDraw
from PIL import ImagePath 


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

def prototipos(width, height):
        
    # Make empty black image of size (100,100)
    img = np.ones((width, height, 3), np.uint8)
    
    #Lists of 9 random widths and heights
    randwidth  = np.random.randint(0,width,(9))
    randheight = np.random.randint(0,height,(9))
    

    
    def checkW(randwidth, width):
        for widthIter in range(0,len(randwidth)):
            for widthIter2 in range(0,len(randwidth)):
                if widthIter == widthIter2:
                    continue
                else:
                    while randwidth[widthIter] < 50 or randwidth[widthIter] > width - 50 or randwidth[widthIter] < randwidth[widthIter2] + 50 and randwidth[widthIter] > randwidth[widthIter2] - 50:
                        randwidth[widthIter]  = np.random.randint(0,width)
                        checkW(randwidth, width)
        return randwidth
    
    def checkH(randheight, height):
        for heightIter in range(0,len(randheight)):
            for heightIter2 in range(0,len(randheight)):
                if heightIter == heightIter2:
                    continue
                else:
                    while randheight[heightIter] < 50 or randheight[heightIter] > height - 50 or randheight[heightIter] < randheight[heightIter2] + 50 and randheight[heightIter] > randheight[heightIter2] - 50:
                        randheight[heightIter]  = np.random.randint(0,height)
                        checkH(randheight, height)
        return randheight
    
    randwidth = checkW(randwidth, width)
    randheight = checkH(randheight, height)
    
  
    
    dotImg = []
    for i in range(0,10):
        appendList = []
        for j in range(0,10):
            appendList.append([255,0,0])
        dotImg.append(appendList)
        
    """
    Las siguientes funciones me dan una posicion dentro de las areas 1, 2, 3, 4 y 5
    """
    #A1: Area 1, el punto se queda en su posicion inicial
    def A1(randwidth, randheight):
        posicionA1 = [randwidth, randheight]
        return posicionA1
        
    #A2: Area 2, el punto se mueve a una de las 8 posiciones al rededor de su posicion inicial
    def A2(randwidth, randheight):
        AreaL2=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0:
                    continue
                else:
                    AreaL2.append([randwidth+i*5, randheight+j*5])
                    
        indiceA2= np.random.randint(0, 8)
        print(AreaL2)
        posicionA2 = AreaL2[indiceA2]
        return posicionA2
    
    #A3: Area 3, el punto se mueve a una de las 16 posiciones al rededor del area 2 y 1.
    def A3(randwidth, randheight):
        AreaL3=[]
        for i in range(-2,3):
            for j in range(-2,3):
                if i==2 or j==2 or i==-2 or j==-2:
                    AreaL3.append([randwidth+i*5, randheight+j*5])
                else:
                    continue
        indiceA3= np.random.randint(0, 16)
        posicionA3=AreaL3[indiceA3]
        return posicionA3

    def A4(randwidth, randheight):
        import random
        AreaL4 = []
        for i in range(-5,6):
            for j in range(-5,6):
                if abs(i) in [3,4,5] or abs(j) in [3,4,5]:
                    AreaL4.append([randwidth+i*5, randheight+j*5])
                
        # Pick a corner to delete
        deletedCorner = random.choice((-5,5))
        for area4Iter in range(0,len(AreaL4)):
            if deletedCorner in AreaL4[area4Iter] and AreaL4[area4Iter] != [deletedCorner,deletedCorner*-1]:
                AreaL4.remove(AreaL4[area4Iter])
    
        indiceA4   = np.random.randint(0, 96)
        posicionA4 = AreaL4[indiceA4]
        return posicionA4
    
    def A5(randwidth, randheight):
        AreaL5=[]
        for i in range(-10,11):
            for j in range(-10,11):
                if abs(i) in [6,7,8,9,10] or abs(j) in [6,7,8,9,10]:
                    AreaL5.append([randwidth+i*5, randheight+j*5])
                
        # Pick a corner to delete
        counter = 0
        for delIter in range(0,20):
            asd = np.random.randint(0,320-counter)
            print(len(AreaL5))
            print(asd)
            print(AreaL5[asd])
            AreaL5.remove(AreaL5[asd])
            counter = counter + 1
    
        indiceA5   = np.random.randint(0, 300)
        posicionA5 = AreaL5[indiceA5]
        return posicionA5

    """
    Funciones que producen las distorsiones L1, L2, L3, L4, L5 y L7
    
    """
    def L2(puntos):
        import random
        Areas=["A1","A2","A3","A4","A5"]
        positions=[]
        for i in range (0,len(puntos[0])):
            Area=random.choices(Areas, weights=(75,15,5,3,2), cum_weights=None, k=1)
            if Area[0]=="A1":
                positions.append(A1(puntos[0][i],puntos[1][i]))
                print(positions)
            elif Area[0]=="A2":
                positions.append(A2(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A3":
                positions.append(A3(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A4":
                positions.append(A4(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A5":
                positions.append(A5(puntos[0][i],puntos[1][i]))
        
        return positions
    
    
    def L3(puntos):
        import random
        Areas=["A1","A2","A3","A4","A5"]
        positions=[]
        for i in range (0,len(puntos[0])):
            Area=random.choices(Areas, weights=(59,20,16,3,2), cum_weights=None, k=1)
            if Area[0]=="A1":
                positions.append(A1(puntos[0][i],puntos[1][i]))
                print(positions)
            elif Area[0]=="A2":
                positions.append(A2(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A3":
                positions.append(A3(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A4":
                positions.append(A4(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A5":
                positions.append(A5(puntos[0][i],puntos[1][i]))        
        return positions
    
    
    def L4(puntos):
        import random
        Areas=["A1","A2","A3","A4","A5"]
        positions=[]
        for i in range (0,len(puntos[0])):
            Area=random.choices(Areas, weights=(36,48,6,5,5), cum_weights=None, k=1)
            if Area[0]=="A1":
                positions.append(A1(puntos[0][i],puntos[1][i]))
                print(positions)
            elif Area[0]=="A2":
                positions.append(A2(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A3":
                positions.append(A3(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A4":
                positions.append(A4(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A5":
                positions.append(A5(puntos[0][i],puntos[1][i]))  
        return positions
    
    
    def L5(puntos):
        import random
        Areas=["A1","A2","A3","A4","A5"]
        positions=[]
        for i in range (0,len(puntos[0])):
            Area=random.choices(Areas, weights=(20,30,40,5,5), cum_weights=None, k=1)
            if Area[0]=="A1":
                positions.append(A1(puntos[0][i],puntos[1][i]))
                print(positions)
            elif Area[0]=="A2":
                positions.append(A2(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A3":
                positions.append(A3(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A4":
                positions.append(A4(puntos[0][i],puntos[1][i]))
            elif Area[0]=="A5":
                positions.append(A5(puntos[0][i],puntos[1][i])) 
        return positions
    
    
    def L7(puntos):
        i=0
        while i<10:
            import random
            Areas=["A1","A2","A3","A4","A5"]
            positions=[]
            for i in range (0,len(puntos[0])):
                Area=random.choices(Areas, weights=(0,24,16,30,30), cum_weights=None, k=1)
                if Area[0]=="A1":
                    positions.append(A1(puntos[0][i],puntos[1][i]))
                    print(positions)
                elif Area[0]=="A2":
                    positions.append(A2(puntos[0][i],puntos[1][i]))
                elif Area[0]=="A3":
                    positions.append(A3(puntos[0][i],puntos[1][i]))
                elif Area[0]=="A4":
                    positions.append(A4(puntos[0][i],puntos[1][i]))
                elif Area[0]=="A5":
                    positions.append(A5(puntos[0][i],puntos[1][i])) 
            return positions

    distortions = [L2,L3,L4,L5,L7]
    allImages = []
    for LIter in range(0,5):
        imgCopy = copy.deepcopy(img)
        positions = distortions[LIter]([randwidth,randheight])
        for imgIter in range(0,len(randwidth)):                
            imgCopy[positions[imgIter][0]-5:positions[imgIter][0] + 5, positions[imgIter][1]-5:positions[imgIter][1]+5] = dotImg
        
        allImages.append(array(imgCopy))

    return allImages

prototipo = prototipos(width, height)

'''
Visualizacion del estimulo
'''
for protoIter in range(0,5):
    stimulus = visual.ImageStim(win=win, image=prototipo[protoIter], mask=None, pos=(0,0), size=(width,height) ,colorSpace='rgb')
    stimulus.draw()
    
    win.flip()
    
    core.wait (10)
    
win.close()



