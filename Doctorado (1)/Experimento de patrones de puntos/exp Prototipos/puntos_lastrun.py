#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.0),
    on marzo 04, 2021, at 20:09
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.0'
expName = 'puntos'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Antonella\\Desktop\\Doctorado\\exp Prototipos\\puntos_lastrun.py',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
poli1 = visual.Polygon(
    win=win, name='poli1',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=0.0, interpolate=True)
poli2 = visual.Polygon(
    win=win, name='poli2',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-1.0, interpolate=True)
poli3 = visual.Polygon(
    win=win, name='poli3',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-2.0, interpolate=True)
poli4 = visual.Polygon(
    win=win, name='poli4',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-3.0, interpolate=True)
poli5 = visual.Polygon(
    win=win, name='poli5',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-4.0, interpolate=True)
poli6 = visual.Polygon(
    win=win, name='poli6',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-5.0, interpolate=True)
poli7 = visual.Polygon(
    win=win, name='poli7',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-6.0, interpolate=True)
poli8 = visual.Polygon(
    win=win, name='poli8',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-7.0, interpolate=True)
poli9 = visual.Polygon(
    win=win, name='poli9',
    edges=99, size=(0.1, 0.1),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-8.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('parametrospuntos.xlsx'),
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
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    poli1.setPos([punto1])
    poli2.setPos([punto2])
    poli3.setPos([punto3])
    poli4.setPos([punto4])
    poli5.setPos([punto5])
    poli6.setPos([punto6])
    poli7.setPos([punto7])
    poli8.setPos([punto8])
    poli9.setPos([punto9])
    # keep track of which components have finished
    trialComponents = [poli1, poli2, poli3, poli4, poli5, poli6, poli7, poli8, poli9]
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
        
        # *poli1* updates
        if poli1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli1.frameNStart = frameN  # exact frame index
            poli1.tStart = t  # local t and not account for scr refresh
            poli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli1, 'tStartRefresh')  # time at next scr refresh
            poli1.setAutoDraw(True)
        if poli1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli1.tStop = t  # not accounting for scr refresh
                poli1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli1, 'tStopRefresh')  # time at next scr refresh
                poli1.setAutoDraw(False)
        
        # *poli2* updates
        if poli2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli2.frameNStart = frameN  # exact frame index
            poli2.tStart = t  # local t and not account for scr refresh
            poli2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli2, 'tStartRefresh')  # time at next scr refresh
            poli2.setAutoDraw(True)
        if poli2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli2.tStop = t  # not accounting for scr refresh
                poli2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli2, 'tStopRefresh')  # time at next scr refresh
                poli2.setAutoDraw(False)
        
        # *poli3* updates
        if poli3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli3.frameNStart = frameN  # exact frame index
            poli3.tStart = t  # local t and not account for scr refresh
            poli3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli3, 'tStartRefresh')  # time at next scr refresh
            poli3.setAutoDraw(True)
        if poli3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli3.tStop = t  # not accounting for scr refresh
                poli3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli3, 'tStopRefresh')  # time at next scr refresh
                poli3.setAutoDraw(False)
        
        # *poli4* updates
        if poli4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli4.frameNStart = frameN  # exact frame index
            poli4.tStart = t  # local t and not account for scr refresh
            poli4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli4, 'tStartRefresh')  # time at next scr refresh
            poli4.setAutoDraw(True)
        if poli4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli4.tStop = t  # not accounting for scr refresh
                poli4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli4, 'tStopRefresh')  # time at next scr refresh
                poli4.setAutoDraw(False)
        
        # *poli5* updates
        if poli5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli5.frameNStart = frameN  # exact frame index
            poli5.tStart = t  # local t and not account for scr refresh
            poli5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli5, 'tStartRefresh')  # time at next scr refresh
            poli5.setAutoDraw(True)
        if poli5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli5.tStop = t  # not accounting for scr refresh
                poli5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli5, 'tStopRefresh')  # time at next scr refresh
                poli5.setAutoDraw(False)
        
        # *poli6* updates
        if poli6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli6.frameNStart = frameN  # exact frame index
            poli6.tStart = t  # local t and not account for scr refresh
            poli6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli6, 'tStartRefresh')  # time at next scr refresh
            poli6.setAutoDraw(True)
        if poli6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli6.tStop = t  # not accounting for scr refresh
                poli6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli6, 'tStopRefresh')  # time at next scr refresh
                poli6.setAutoDraw(False)
        
        # *poli7* updates
        if poli7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli7.frameNStart = frameN  # exact frame index
            poli7.tStart = t  # local t and not account for scr refresh
            poli7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli7, 'tStartRefresh')  # time at next scr refresh
            poli7.setAutoDraw(True)
        if poli7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli7.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli7.tStop = t  # not accounting for scr refresh
                poli7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli7, 'tStopRefresh')  # time at next scr refresh
                poli7.setAutoDraw(False)
        
        # *poli8* updates
        if poli8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli8.frameNStart = frameN  # exact frame index
            poli8.tStart = t  # local t and not account for scr refresh
            poli8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli8, 'tStartRefresh')  # time at next scr refresh
            poli8.setAutoDraw(True)
        if poli8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli8.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli8.tStop = t  # not accounting for scr refresh
                poli8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli8, 'tStopRefresh')  # time at next scr refresh
                poli8.setAutoDraw(False)
        
        # *poli9* updates
        if poli9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            poli9.frameNStart = frameN  # exact frame index
            poli9.tStart = t  # local t and not account for scr refresh
            poli9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(poli9, 'tStartRefresh')  # time at next scr refresh
            poli9.setAutoDraw(True)
        if poli9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > poli9.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                poli9.tStop = t  # not accounting for scr refresh
                poli9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(poli9, 'tStopRefresh')  # time at next scr refresh
                poli9.setAutoDraw(False)
        
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
    trials.addData('poli1.started', poli1.tStartRefresh)
    trials.addData('poli1.stopped', poli1.tStopRefresh)
    trials.addData('poli2.started', poli2.tStartRefresh)
    trials.addData('poli2.stopped', poli2.tStopRefresh)
    trials.addData('poli3.started', poli3.tStartRefresh)
    trials.addData('poli3.stopped', poli3.tStopRefresh)
    trials.addData('poli4.started', poli4.tStartRefresh)
    trials.addData('poli4.stopped', poli4.tStopRefresh)
    trials.addData('poli5.started', poli5.tStartRefresh)
    trials.addData('poli5.stopped', poli5.tStopRefresh)
    trials.addData('poli6.started', poli6.tStartRefresh)
    trials.addData('poli6.stopped', poli6.tStopRefresh)
    trials.addData('poli7.started', poli7.tStartRefresh)
    trials.addData('poli7.stopped', poli7.tStopRefresh)
    trials.addData('poli8.started', poli8.tStartRefresh)
    trials.addData('poli8.stopped', poli8.tStopRefresh)
    trials.addData('poli9.started', poli9.tStartRefresh)
    trials.addData('poli9.stopped', poli9.tStopRefresh)
# completed 1.0 repeats of 'trials'


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
