#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on diciembre 06, 2022, at 13:49
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'PruebaGabor2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\UdeSA\\Desktop\\Antonella\\Doctorado (1)\\Exp de Gabor\\Exp de Gabor\\Scripts Psychopy\\PruebaGabor2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Intrucciones"
IntruccionesClock = core.Clock()
Instrucciones1 = visual.TextStim(win=win, name='Instrucciones1',
    text='Bienvenidos/as\nPresiona la barra espaciadora para continuar',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
Instrucciones2 = visual.TextStim(win=win, name='Instrucciones2',
    text='A continuacion\nveran un circulo en pantalla, por dentro tienen lineas oscuras y claras.',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()
Instrucciones3 = visual.TextStim(win=win, name='Instrucciones3',
    text='Observa la cantidad de lineas claras y oscuras que hay.\n\nHay dos tipos de circulos, se diferencian en la frecuencia de las lineas claras y oscuras.\n\n\n\n\n',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_5 = keyboard.Keyboard()
instrucciones4 = visual.TextStim(win=win, name='instrucciones4',
    text='Se te va a mostrar un circulo en la pantalla y debes agruparlo segun la frecuencia de sus lineas.\n\nUn grupo se corresponde con la flecha derecha. Cuando lo veas presiona la tecla derecha.\n\nEl otro grupo se corresponde con la flecha izquierda. Cuando lo veas presiona la flecha izquierda.',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
key_resp_6 = keyboard.Keyboard()
Instrucciones5 = visual.TextStim(win=win, name='Instrucciones5',
    text='Cuando veas el primer circulo tenes que adivinar si se corresponde con la flecha derecha o izquierda.\n\nVamos a hacer uno de prueba!',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Prueba"
PruebaClock = core.Clock()
KeyRespPrueba = keyboard.Keyboard()
GratingPrueba = visual.GratingStim(
    win=win, name='GratingPrueba',units='pix', 
    tex='sin', mask='circle', anchor='center',
    ori=1.0, pos=(0,0), size=(200,200), sf=1.0, phase=0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1, contrast=1.0, blendmode='avg',
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "FeedbackPrueba"
FeedbackPruebaClock = core.Clock()
msg=''
FeedbackPrueb = visual.TextStim(win=win, name='FeedbackPrueb',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Comienzo"
ComienzoClock = core.Clock()
ComienzoTexto = visual.TextStim(win=win, name='ComienzoTexto',
    text='Excelente\nSi tenes alguna duda consulta antes de seguir con el/la experimentador/a\n\nCuando estes listo/a para continuar presiona la barra espaciadora',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trialb"
trialbClock = core.Clock()
grating2 = visual.GratingStim(
    win=win, name='grating2',units='pix', 
    tex='sin', mask='circle', anchor='center',
    ori=1.0, pos=(0,0), size=(200, 200), sf=1.0, phase=0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1, contrast=1.0, blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "feedbacka"
feedbackaClock = core.Clock()
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
Gracias = visual.TextStim(win=win, name='Gracias',
    text='¡Muchas gracias por participar!',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intrucciones"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
IntruccionesComponents = [Instrucciones1, key_resp_3, Instrucciones2, key_resp_4, Instrucciones3, key_resp_5, instrucciones4, key_resp_6, Instrucciones5, key_resp_7]
for thisComponent in IntruccionesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntruccionesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intrucciones"-------
while continueRoutine:
    # get current time
    t = IntruccionesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntruccionesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrucciones1* updates
    if Instrucciones1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        Instrucciones1.frameNStart = frameN  # exact frame index
        Instrucciones1.tStart = t  # local t and not account for scr refresh
        Instrucciones1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrucciones1, 'tStartRefresh')  # time at next scr refresh
        Instrucciones1.setAutoDraw(True)
    if Instrucciones1.status == STARTED:
        if bool(key_resp_3.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            Instrucciones1.tStop = t  # not accounting for scr refresh
            Instrucciones1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instrucciones1, 'tStopRefresh')  # time at next scr refresh
            Instrucciones1.setAutoDraw(False)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED:
        if bool(key_resp_3.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            key_resp_3.tStop = t  # not accounting for scr refresh
            key_resp_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
            key_resp_3.status = FINISHED
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
    
    # *Instrucciones2* updates
    if Instrucciones2.status == NOT_STARTED and Instrucciones1.status==FINISHED:
        # keep track of start time/frame for later
        Instrucciones2.frameNStart = frameN  # exact frame index
        Instrucciones2.tStart = t  # local t and not account for scr refresh
        Instrucciones2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrucciones2, 'tStartRefresh')  # time at next scr refresh
        Instrucciones2.setAutoDraw(True)
    if Instrucciones2.status == STARTED:
        if bool(key_resp_4.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            Instrucciones2.tStop = t  # not accounting for scr refresh
            Instrucciones2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instrucciones2, 'tStopRefresh')  # time at next scr refresh
            Instrucciones2.setAutoDraw(False)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and Instrucciones2.status==STARTED:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED:
        if bool(key_resp_4.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            key_resp_4.tStop = t  # not accounting for scr refresh
            key_resp_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
            key_resp_4.status = FINISHED
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
    
    # *Instrucciones3* updates
    if Instrucciones3.status == NOT_STARTED and Instrucciones2.status==FINISHED:
        # keep track of start time/frame for later
        Instrucciones3.frameNStart = frameN  # exact frame index
        Instrucciones3.tStart = t  # local t and not account for scr refresh
        Instrucciones3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrucciones3, 'tStartRefresh')  # time at next scr refresh
        Instrucciones3.setAutoDraw(True)
    if Instrucciones3.status == STARTED:
        if bool(key_resp_5.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            Instrucciones3.tStop = t  # not accounting for scr refresh
            Instrucciones3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instrucciones3, 'tStopRefresh')  # time at next scr refresh
            Instrucciones3.setAutoDraw(False)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and Instrucciones3.status==STARTED:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED:
        if bool(key_resp_5.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            key_resp_5.tStop = t  # not accounting for scr refresh
            key_resp_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
            key_resp_5.status = FINISHED
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
    
    # *instrucciones4* updates
    if instrucciones4.status == NOT_STARTED and Instrucciones3.status==FINISHED:
        # keep track of start time/frame for later
        instrucciones4.frameNStart = frameN  # exact frame index
        instrucciones4.tStart = t  # local t and not account for scr refresh
        instrucciones4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrucciones4, 'tStartRefresh')  # time at next scr refresh
        instrucciones4.setAutoDraw(True)
    if instrucciones4.status == STARTED:
        if bool(key_resp_6.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            instrucciones4.tStop = t  # not accounting for scr refresh
            instrucciones4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instrucciones4, 'tStopRefresh')  # time at next scr refresh
            instrucciones4.setAutoDraw(False)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and instrucciones4.status==STARTED:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED:
        if bool(key_resp_6.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            key_resp_6.tStop = t  # not accounting for scr refresh
            key_resp_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_6, 'tStopRefresh')  # time at next scr refresh
            key_resp_6.status = FINISHED
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
    
    # *Instrucciones5* updates
    if Instrucciones5.status == NOT_STARTED and instrucciones4.status==FINISHED:
        # keep track of start time/frame for later
        Instrucciones5.frameNStart = frameN  # exact frame index
        Instrucciones5.tStart = t  # local t and not account for scr refresh
        Instrucciones5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrucciones5, 'tStartRefresh')  # time at next scr refresh
        Instrucciones5.setAutoDraw(True)
    if Instrucciones5.status == STARTED:
        if bool(key_resp_6.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            Instrucciones5.tStop = t  # not accounting for scr refresh
            Instrucciones5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instrucciones5, 'tStopRefresh')  # time at next scr refresh
            Instrucciones5.setAutoDraw(False)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and Instrucciones5.status==STARTED:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED:
        if bool(key_resp_6.getKeys(keyList=['space'], waitRelease=False)):
            # keep track of stop time/frame for later
            key_resp_7.tStop = t  # not accounting for scr refresh
            key_resp_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_7, 'tStopRefresh')  # time at next scr refresh
            key_resp_7.status = FINISHED
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntruccionesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intrucciones"-------
for thisComponent in IntruccionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instrucciones1.started', Instrucciones1.tStartRefresh)
thisExp.addData('Instrucciones1.stopped', Instrucciones1.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Instrucciones2.started', Instrucciones2.tStartRefresh)
thisExp.addData('Instrucciones2.stopped', Instrucciones2.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Instrucciones3.started', Instrucciones3.tStartRefresh)
thisExp.addData('Instrucciones3.stopped', Instrucciones3.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrucciones4.started', instrucciones4.tStartRefresh)
thisExp.addData('instrucciones4.stopped', instrucciones4.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Instrucciones5.started', Instrucciones5.tStartRefresh)
thisExp.addData('Instrucciones5.stopped', Instrucciones5.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intrucciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Training = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Parametros/Parametros E y F(superpuestos)/ParametrosEyFPractice.xlsx'),
    seed=None, name='Training')
thisExp.addLoop(Training)  # add the loop to the experiment
thisTraining = Training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
if thisTraining != None:
    for paramName in thisTraining:
        exec('{} = thisTraining[paramName]'.format(paramName))

for thisTraining in Training:
    currentLoop = Training
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Prueba"-------
    continueRoutine = True
    routineTimer.add(3.200000)
    # update component parameters for each repeat
    KeyRespPrueba.keys = []
    KeyRespPrueba.rt = []
    _KeyRespPrueba_allKeys = []
    GratingPrueba.setOri(Orientation)
    GratingPrueba.setSF(FrecuenciaEspacial)
    # keep track of which components have finished
    PruebaComponents = [KeyRespPrueba, GratingPrueba]
    for thisComponent in PruebaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PruebaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prueba"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PruebaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PruebaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyRespPrueba* updates
        waitOnFlip = False
        if KeyRespPrueba.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            KeyRespPrueba.frameNStart = frameN  # exact frame index
            KeyRespPrueba.tStart = t  # local t and not account for scr refresh
            KeyRespPrueba.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyRespPrueba, 'tStartRefresh')  # time at next scr refresh
            KeyRespPrueba.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyRespPrueba.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyRespPrueba.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KeyRespPrueba.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > KeyRespPrueba.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                KeyRespPrueba.tStop = t  # not accounting for scr refresh
                KeyRespPrueba.frameNStop = frameN  # exact frame index
                win.timeOnFlip(KeyRespPrueba, 'tStopRefresh')  # time at next scr refresh
                KeyRespPrueba.status = FINISHED
        if KeyRespPrueba.status == STARTED and not waitOnFlip:
            theseKeys = KeyRespPrueba.getKeys(keyList=['left','right'], waitRelease=False)
            _KeyRespPrueba_allKeys.extend(theseKeys)
            if len(_KeyRespPrueba_allKeys):
                KeyRespPrueba.keys = _KeyRespPrueba_allKeys[-1].name  # just the last key pressed
                KeyRespPrueba.rt = _KeyRespPrueba_allKeys[-1].rt
                # was this correct?
                if (KeyRespPrueba.keys == str(tecla)) or (KeyRespPrueba.keys == tecla):
                    KeyRespPrueba.corr = 1
                else:
                    KeyRespPrueba.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *GratingPrueba* updates
        if GratingPrueba.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            GratingPrueba.frameNStart = frameN  # exact frame index
            GratingPrueba.tStart = t  # local t and not account for scr refresh
            GratingPrueba.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GratingPrueba, 'tStartRefresh')  # time at next scr refresh
            GratingPrueba.setAutoDraw(True)
        if GratingPrueba.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GratingPrueba.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                GratingPrueba.tStop = t  # not accounting for scr refresh
                GratingPrueba.frameNStop = frameN  # exact frame index
                win.timeOnFlip(GratingPrueba, 'tStopRefresh')  # time at next scr refresh
                GratingPrueba.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PruebaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prueba"-------
    for thisComponent in PruebaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyRespPrueba.keys in ['', [], None]:  # No response was made
        KeyRespPrueba.keys = None
        # was no response the correct answer?!
        if str(tecla).lower() == 'none':
           KeyRespPrueba.corr = 1;  # correct non-response
        else:
           KeyRespPrueba.corr = 0;  # failed to respond (incorrectly)
    # store data for Training (TrialHandler)
    Training.addData('KeyRespPrueba.keys',KeyRespPrueba.keys)
    Training.addData('KeyRespPrueba.corr', KeyRespPrueba.corr)
    if KeyRespPrueba.keys != None:  # we had a response
        Training.addData('KeyRespPrueba.rt', KeyRespPrueba.rt)
    Training.addData('KeyRespPrueba.started', KeyRespPrueba.tStartRefresh)
    Training.addData('KeyRespPrueba.stopped', KeyRespPrueba.tStopRefresh)
    Training.addData('GratingPrueba.started', GratingPrueba.tStartRefresh)
    Training.addData('GratingPrueba.stopped', GratingPrueba.tStopRefresh)
    
    # ------Prepare to start Routine "FeedbackPrueba"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if KeyRespPrueba.corr:#stored on last run routine
      msg="¡Correcto!"
    else:
      msg="Segui intentando"
    FeedbackPrueb.setText(msg)
    # keep track of which components have finished
    FeedbackPruebaComponents = [FeedbackPrueb]
    for thisComponent in FeedbackPruebaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackPruebaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FeedbackPrueba"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackPruebaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackPruebaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FeedbackPrueb* updates
        if FeedbackPrueb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FeedbackPrueb.frameNStart = frameN  # exact frame index
            FeedbackPrueb.tStart = t  # local t and not account for scr refresh
            FeedbackPrueb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FeedbackPrueb, 'tStartRefresh')  # time at next scr refresh
            FeedbackPrueb.setAutoDraw(True)
        if FeedbackPrueb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FeedbackPrueb.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FeedbackPrueb.tStop = t  # not accounting for scr refresh
                FeedbackPrueb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FeedbackPrueb, 'tStopRefresh')  # time at next scr refresh
                FeedbackPrueb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackPruebaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FeedbackPrueba"-------
    for thisComponent in FeedbackPruebaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Training.addData('FeedbackPrueb.started', FeedbackPrueb.tStartRefresh)
    Training.addData('FeedbackPrueb.stopped', FeedbackPrueb.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Training'

# get names of stimulus parameters
if Training.trialList in ([], [None], None):
    params = []
else:
    params = Training.trialList[0].keys()
# save data for this loop
Training.saveAsExcel(filename + '.xlsx', sheetName='Training',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Comienzo"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
ComienzoComponents = [ComienzoTexto, key_resp_2]
for thisComponent in ComienzoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ComienzoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Comienzo"-------
while continueRoutine:
    # get current time
    t = ComienzoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ComienzoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ComienzoTexto* updates
    if ComienzoTexto.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        ComienzoTexto.frameNStart = frameN  # exact frame index
        ComienzoTexto.tStart = t  # local t and not account for scr refresh
        ComienzoTexto.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ComienzoTexto, 'tStartRefresh')  # time at next scr refresh
        ComienzoTexto.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ComienzoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Comienzo"-------
for thisComponent in ComienzoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ComienzoTexto.started', ComienzoTexto.tStartRefresh)
thisExp.addData('ComienzoTexto.stopped', ComienzoTexto.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Comienzo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Test = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Parametros/Parametros E y F(superpuestos)/ParametrosEyF.xlsx'),
    seed=None, name='Test')
thisExp.addLoop(Test)  # add the loop to the experiment
thisTest = Test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest:
        exec('{} = thisTest[paramName]'.format(paramName))

for thisTest in Test:
    currentLoop = Test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trialb"-------
    continueRoutine = True
    routineTimer.add(3.200000)
    # update component parameters for each repeat
    grating2.setOri(Orientation)
    grating2.setSF(FrecuenciaEspacial)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialbComponents = [grating2, key_resp]
    for thisComponent in trialbComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialb"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialbClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialbClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating2* updates
        if grating2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            grating2.frameNStart = frameN  # exact frame index
            grating2.tStart = t  # local t and not account for scr refresh
            grating2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating2, 'tStartRefresh')  # time at next scr refresh
            grating2.setAutoDraw(True)
        if grating2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                grating2.tStop = t  # not accounting for scr refresh
                grating2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(grating2, 'tStopRefresh')  # time at next scr refresh
                grating2.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(tecla)) or (key_resp.keys == tecla):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialbComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialb"-------
    for thisComponent in trialbComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test.addData('grating2.started', grating2.tStartRefresh)
    Test.addData('grating2.stopped', grating2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(tecla).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Test (TrialHandler)
    Test.addData('key_resp.keys',key_resp.keys)
    Test.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        Test.addData('key_resp.rt', key_resp.rt)
    Test.addData('key_resp.started', key_resp.tStartRefresh)
    Test.addData('key_resp.stopped', key_resp.tStopRefresh)
    
    # ------Prepare to start Routine "feedbacka"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if key_resp.corr:#stored on last run routine
      msg="¡Correcto!"
    else:
      msg="Segui intentando"
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackaComponents = [feedback_2]
    for thisComponent in feedbackaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbacka"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_2* updates
        if feedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.tStart = t  # local t and not account for scr refresh
            feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_2, 'tStartRefresh')  # time at next scr refresh
            feedback_2.setAutoDraw(True)
        if feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_2.tStop = t  # not accounting for scr refresh
                feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_2, 'tStopRefresh')  # time at next scr refresh
                feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbacka"-------
    for thisComponent in feedbackaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test.addData('feedback_2.started', feedback_2.tStartRefresh)
    Test.addData('feedback_2.stopped', feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Test'

# get names of stimulus parameters
if Test.trialList in ([], [None], None):
    params = []
else:
    params = Test.trialList[0].keys()
# save data for this loop
Test.saveAsExcel(filename + '.xlsx', sheetName='Test',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(4.500000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [Gracias, image]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Gracias* updates
    if Gracias.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Gracias.frameNStart = frameN  # exact frame index
        Gracias.tStart = t  # local t and not account for scr refresh
        Gracias.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Gracias, 'tStartRefresh')  # time at next scr refresh
        Gracias.setAutoDraw(True)
    if Gracias.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Gracias.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            Gracias.tStop = t  # not accounting for scr refresh
            Gracias.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Gracias, 'tStopRefresh')  # time at next scr refresh
            Gracias.setAutoDraw(False)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Gracias.started', Gracias.tStartRefresh)
thisExp.addData('Gracias.stopped', Gracias.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
