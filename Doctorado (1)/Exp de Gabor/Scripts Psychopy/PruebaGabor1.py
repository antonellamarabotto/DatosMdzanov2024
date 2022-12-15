#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on febrero 19, 2021, at 13:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'PruebaGabor1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Antonella\\Desktop\\Doctorado\\Exp de Gabor\\Scripts Psychopy\\PruebaGabor1.py',
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
    size=[1366, 768], fullscr=True, screen=0, 
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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Intrucciones"
IntruccionesClock = core.Clock()
InstruccionesGabor = visual.TextStim(win=win, name='InstruccionesGabor',
    text='Bienvenidos\nDescripcion de la tarea',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
respinstrucciones = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
grating = visual.GratingStim(
    win=win, name='grating',units='pix', 
    tex='sin', mask='circle',
    ori=1.0, pos=(0,0), size=(300, 300), sf=1.0, phase=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intrucciones"-------
continueRoutine = True
# update component parameters for each repeat
respinstrucciones.keys = []
respinstrucciones.rt = []
_respinstrucciones_allKeys = []
# keep track of which components have finished
IntruccionesComponents = [InstruccionesGabor, respinstrucciones]
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
    
    # *InstruccionesGabor* updates
    if InstruccionesGabor.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        InstruccionesGabor.frameNStart = frameN  # exact frame index
        InstruccionesGabor.tStart = t  # local t and not account for scr refresh
        InstruccionesGabor.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstruccionesGabor, 'tStartRefresh')  # time at next scr refresh
        InstruccionesGabor.setAutoDraw(True)
    
    # *respinstrucciones* updates
    waitOnFlip = False
    if respinstrucciones.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        respinstrucciones.frameNStart = frameN  # exact frame index
        respinstrucciones.tStart = t  # local t and not account for scr refresh
        respinstrucciones.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respinstrucciones, 'tStartRefresh')  # time at next scr refresh
        respinstrucciones.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respinstrucciones.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respinstrucciones.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respinstrucciones.status == STARTED and not waitOnFlip:
        theseKeys = respinstrucciones.getKeys(keyList=None, waitRelease=False)
        _respinstrucciones_allKeys.extend(theseKeys)
        if len(_respinstrucciones_allKeys):
            respinstrucciones.keys = _respinstrucciones_allKeys[-1].name  # just the last key pressed
            respinstrucciones.rt = _respinstrucciones_allKeys[-1].rt
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
thisExp.addData('InstruccionesGabor.started', InstruccionesGabor.tStartRefresh)
thisExp.addData('InstruccionesGabor.stopped', InstruccionesGabor.tStopRefresh)
# check responses
if respinstrucciones.keys in ['', [], None]:  # No response was made
    respinstrucciones.keys = None
thisExp.addData('respinstrucciones.keys',respinstrucciones.keys)
if respinstrucciones.keys != None:  # we had a response
    thisExp.addData('respinstrucciones.rt', respinstrucciones.rt)
thisExp.addData('respinstrucciones.started', respinstrucciones.tStartRefresh)
thisExp.addData('respinstrucciones.stopped', respinstrucciones.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intrucciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Gaborparametros.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    grating.setOri(Orientation)
    grating.setSF(FrecEspacial)
    grating.setPhase(Fase)
    # keep track of which components have finished
    trialComponents = [grating]
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
        
        # *grating* updates
        if grating.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            grating.setAutoDraw(True)
        if grating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                grating.tStop = t  # not accounting for scr refresh
                grating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(grating, 'tStopRefresh')  # time at next scr refresh
                grating.setAutoDraw(False)
        
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
    trials.addData('grating.started', grating.tStartRefresh)
    trials.addData('grating.stopped', grating.tStopRefresh)
    thisExp.nextEntry()
    
# completed 10 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
