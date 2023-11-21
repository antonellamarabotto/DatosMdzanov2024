﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on julio 25, 2023, at 15:02
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
expName = 'PruebaBlurryBorders'  # from the Builder filename that created this script
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
    originPath='D:\\Antonella\\Experimentos\\Exp de Gabor\\Integracion de la informacion\\PruebaBlurryBorders.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Begin Experiment tab code
mask_grating.opacity = 1  # Set the opacity of the mask to 1 (fully opaque)


grating = visual.GratingStim(
    win=win, name='grating',units='pix', 
    tex='sin', mask='circle', anchor='center',
    ori=96.0, pos=(0, 0), size=(200,200), sf=0.030600787, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
grating_2 = visual.GratingStim(
    win=win, name='grating_2',units='pix', 
    tex='sin', mask='gauss', anchor='center',
    ori=96.0, pos=(0, 0), size=(250,250), sf=0.030600787, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=0.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# Begin Routine tab code
grating.tex = mask_grating.tex  # Use the texture of the mask_grating for the main grating
grating.mask = mask_grating  # Use the mask_grating as the mask for the main grating
# keep track of which components have finished
trialComponents = [grating, grating_2]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    grating.tex = mask_grating.tex  # Update the main grating texture with the mask texture
    grating.draw()  # Draw the circular grating stimulus
    win.flip()  # Update the window to display the stimulus
    
    # *grating* updates
    if grating.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        grating.frameNStart = frameN  # exact frame index
        grating.tStart = t  # local t and not account for scr refresh
        grating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
        grating.setAutoDraw(True)
    if grating.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > grating.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            grating.tStop = t  # not accounting for scr refresh
            grating.frameNStop = frameN  # exact frame index
            win.timeOnFlip(grating, 'tStopRefresh')  # time at next scr refresh
            grating.setAutoDraw(False)
    
    # *grating_2* updates
    if grating_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        grating_2.frameNStart = frameN  # exact frame index
        grating_2.tStart = t  # local t and not account for scr refresh
        grating_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grating_2, 'tStartRefresh')  # time at next scr refresh
        grating_2.setAutoDraw(True)
    if grating_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > grating_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            grating_2.tStop = t  # not accounting for scr refresh
            grating_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(grating_2, 'tStopRefresh')  # time at next scr refresh
            grating_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('grating.started', grating.tStartRefresh)
thisExp.addData('grating.stopped', grating.tStopRefresh)
thisExp.addData('grating_2.started', grating_2.tStartRefresh)
thisExp.addData('grating_2.stopped', grating_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
