#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.0),
    on marzo 05, 2021, at 10:52
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
expName = 'circles'  # from the Builder filename that created this script
expInfo = {'Name': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['Name'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Antonella\\Desktop\\Doctorado\\exp Prototipos\\circles_metacog-master\\circles_metacog-master\\circles.py',
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
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "test_trial"
test_trialClock = core.Clock()
Bienvenidos_prueba = visual.ImageStim(
    win=win,
    name='Bienvenidos_prueba', units='pix', 
    image='images/Bienvenidos-prueba.png', mask=None,
    ori=0, pos=(0, 0), size=[1024, 768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trialpresentation"
trialpresentationClock = core.Clock()


#points_to_pass_level sets the number of point that you have to do in order to advance one level.
#If this experiment will be run with children we recomend to use 10, but if it will be run with adults you can use a big level equal to the size of trial_types times 3.
points_to_pass_level = 10

treatment = 'Control'

circlep0 = visual.Polygon(
    win=win, name='circlep0',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=[-120, 120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-1.0, interpolate=True)
circlep1 = visual.Polygon(
    win=win, name='circlep1',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=[0, 120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-2.0, interpolate=True)
circlep2 = visual.Polygon(
    win=win, name='circlep2',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=(120, 120),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-3.0, interpolate=True)
circlep3 = visual.Polygon(
    win=win, name='circlep3',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=(-100, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-4.0, interpolate=True)
circlep4 = visual.Polygon(
    win=win, name='circlep4',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-5.0, interpolate=True)
circlep5 = visual.Polygon(
    win=win, name='circlep5',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=(100, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-6.0, interpolate=True)
circlep6 = visual.Polygon(
    win=win, name='circlep6',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=(-120, -120),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-7.0, interpolate=True)
circlep7 = visual.Polygon(
    win=win, name='circlep7',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=(0, -120),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-8.0, interpolate=True)
circlep8 = visual.Polygon(
    win=win, name='circlep8',units='pix', 
    edges=100, size=(8, 8),
    ori=0, pos=(120, -120),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-9.0, interpolate=True)
#size pattern it sets the relative size of the cirlces.
size_pattern = [96, 92, 88, 80, 75, 70, 60, 50]
max_size = 100
circle_distance = max_size*2.5#150
min_dist = circle_distance - 2*max_size
xoffset = -circle_distance
yoffset = -float(win.size[1]) / 2 + max_size*1.5
circle_positions = [(circle_distance * (i % 3) + xoffset, circle_distance * (i - i % 3) / 3 + yoffset) for i in range(9)]
circle_units = 'pix'


score = 0

#wager_cirlces are the circles that shows you your current score.
xoffset = -float(win.size[0])/2 + 100
yoffset = -float(win.size[1])/2 + 100
def wpoligon(i, points_to_pass_level=points_to_pass_level):
    if points_to_pass_level < 31:
        pos = [xoffset, 40 * i + yoffset]
    else:
        pos = [40 * (i % 6) + xoffset, 40 * (i - i % 6) / 6 + yoffset]
    return visual.Polygon(win, name='wcircle'+str(i), units='pix', edges=100,
                          size=[30, 30], pos=pos, fillColor=[0,0,0], lineColor=[0,0,0])
wager_circles = [wpoligon(i) for i in range(points_to_pass_level)]

for wcircle in wager_circles:
    wcircle.setAutoDraw(True)

#Set de number of routines per loop

trialpresentation_types =['wagerpres','sliderpres', 'plainpres']*2
trialpresentation_levels =[0.35, 0.35,0.5 ,0.8 , 0.8]
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "sliderpres"
sliderpresClock = core.Clock()
rating_2 = visual.RatingScale(win=win, name='rating_2', labels=('nada seguro', 'muy seguro'), markerColor='White', lineColor=[-1,-1,-1], textColor=[-1,-1,-1], scale=None, singleClick=True, precision=100, showAccept=False, mouseOnly=True)
slider_3 = visual.ImageStim(
    win=win,
    name='slider_3', units='norm', 
    image='images/slider2.png', mask=None,
    ori=0, pos=(0, -0.4), size=(0.61, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "wagerpres"
wagerpresClock = core.Clock()
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
betbutton = visual.ImageStim(
    win=win,
    name='betbutton', units='pix', 
    image='images/green-tick.png', mask=None,
    ori=0, pos=[-75, -float(win.size[1])/2+100], size=(120, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
surebutton = visual.ImageStim(
    win=win,
    name='surebutton', units='pix', 
    image='images/red-cross.png', mask=None,
    ori=0, pos=[75,  -float(win.size[1])/2+100], size=(120, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "Start_2"
Start_2Clock = core.Clock()
Start = visual.ImageStim(
    win=win,
    name='Start', units='pix', 
    image='images/Start-playing.png', mask=None,
    ori=0, pos=(0, 0), size=[1024, 768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
#set the mix of tirlas that you want.
wager = 18
slider = 18
plain = 6
wagereasy = 2
wagerhard = 2
slidereasy = 2
sliderhard = 2
plaineasy = 2
plainhard = 2

#points_to_pass_level sets the number of point that you have to do in order to advance one level.
#If this experiment will be run with children we recomend to use 10, but if it will be run with adults you can use a big level equal to the size of trial_types times 3.
points_to_pass_level = 10

treatment = 'Control'
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
circle0 = visual.Polygon(
    win=win, name='circle0',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[-120, 120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-2.0, interpolate=True)
circle1 = visual.Polygon(
    win=win, name='circle1',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[0, 120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-3.0, interpolate=True)
circle2 = visual.Polygon(
    win=win, name='circle2',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[120, 120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-4.0, interpolate=True)
circle3 = visual.Polygon(
    win=win, name='circle3',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[-100, 0],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-5.0, interpolate=True)
circle4 = visual.Polygon(
    win=win, name='circle4',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[0, 0],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-6.0, interpolate=True)
circle5 = visual.Polygon(
    win=win, name='circle5',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[100, 0],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-7.0, interpolate=True)
circle6 = visual.Polygon(
    win=win, name='circle6',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[-120, -120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-8.0, interpolate=True)
circle7 = visual.Polygon(
    win=win, name='circle7',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[0, -120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-9.0, interpolate=True)
circle8 = visual.Polygon(
    win=win, name='circle8',units='pix', 
    edges=100, size=[8, 8],
    ori=0, pos=[120, -120],
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-10.0, interpolate=True)
#size pattern it sets the relative size of the cirlces.
size_pattern = [96, 92, 88, 80, 75, 70, 60, 50]
max_size = 100
circle_distance = max_size*2.5#150
min_dist = circle_distance - 2*max_size
xoffset = -circle_distance
yoffset = -float(win.size[1]) / 2 + max_size*1.5
circle_positions = [(circle_distance * (i % 3) + xoffset, circle_distance * (i - i % 3) / 3 + yoffset) for i in range(9)]
circle_units = 'pix'


score = 0

#wager_cirlces are the circles that shows you your current score.
xoffset = -float(win.size[0])/2 + 100
yoffset = -float(win.size[1])/2 + 100
def wpoligon(i, points_to_pass_level=points_to_pass_level):
    if points_to_pass_level < 31:
        pos = [xoffset, 40 * i + yoffset]
    else:
        pos = [40 * (i % 6) + xoffset, 40 * (i - i % 6) / 6 + yoffset]
    return visual.Polygon(win, name='wcircle'+str(i), units='pix', edges=100,
                          size=[30, 30], pos=pos, fillColor=[0,0,0], lineColor=[0,0,0])
wager_circles = [wpoligon(i) for i in range(points_to_pass_level)]

for wcircle in wager_circles:
    wcircle.setAutoDraw(True)


trial_types = wager * ['wager'] + slider * ['slider'] + plain * ['plain']
trial_types +=  wagereasy * ['wagereasy'] 
trial_types +=  wagerhard * ['wagerhard'] 
trial_types +=  slidereasy * ['slidereasy'] 
trial_types +=  sliderhard * ['sliderhard']


np.random.shuffle(trial_types)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "slider"
sliderClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', labels=('nada seguro', 'muy seguro'), markerColor='White', lineColor=[-1,-1,-1], textColor=[-1,-1,-1], scale=None, singleClick=True, precision=100, showAccept=False, mouseOnly=True, low=0, high=1)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='norm', 
    image='images/slider2.png', mask=None,
    ori=0, pos=(0, -0.4), size=(0.61, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "wager"
wagerClock = core.Clock()
mouse_wager = event.Mouse(win=win)
x, y = [None, None]
mouse_wager.mouseClock = core.Clock()
bet_button = visual.ImageStim(
    win=win,
    name='bet_button', units='pix', 
    image='images/green-tick.png', mask=None,
    ori=0, pos=[-75, -float(win.size[1])/2+100], size=[120, 150],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sure_button = visual.ImageStim(
    win=win,
    name='sure_button', units='pix', 
    image='images/red-cross.png', mask=None,
    ori=0, pos=[75,  -float(win.size[1])/2+100], size=[120, 150],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "pass_level"
pass_levelClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='images/congrats.jpg', mask=None,
    ori=0, pos=[0, 0], size=[1024, 768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='pix', 
    image='images/Finish.png', mask=None,
    ori=0, pos=(0, 0), size=[1024, 768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "test_trial"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
test_trialComponents = [Bienvenidos_prueba]
for thisComponent in test_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = test_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Bienvenidos_prueba* updates
    if Bienvenidos_prueba.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Bienvenidos_prueba.frameNStart = frameN  # exact frame index
        Bienvenidos_prueba.tStart = t  # local t and not account for scr refresh
        Bienvenidos_prueba.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Bienvenidos_prueba, 'tStartRefresh')  # time at next scr refresh
        Bienvenidos_prueba.setAutoDraw(True)
    if Bienvenidos_prueba.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Bienvenidos_prueba.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Bienvenidos_prueba.tStop = t  # not accounting for scr refresh
            Bienvenidos_prueba.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Bienvenidos_prueba, 'tStopRefresh')  # time at next scr refresh
            Bienvenidos_prueba.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_trial"-------
for thisComponent in test_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Bienvenidos_prueba.started', Bienvenidos_prueba.tStartRefresh)
thisExp.addData('Bienvenidos_prueba.stopped', Bienvenidos_prueba.tStopRefresh)

# set up handler to look after randomisation of conditions etc
intro = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='intro')
thisExp.addLoop(intro)  # add the loop to the experiment
thisIntro = intro.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIntro.rgb)
if thisIntro != None:
    for paramName in thisIntro:
        exec('{} = thisIntro[paramName]'.format(paramName))

for thisIntro in intro:
    currentLoop = intro
    # abbreviate parameter names if possible (e.g. rgb = thisIntro.rgb)
    if thisIntro != None:
        for paramName in thisIntro:
            exec('{} = thisIntro[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trialpresentation"-------
    continueRoutine = True
    routineTimer.add(10.500000)
    # update component parameters for each repeat
    trialpresentation_type = trialpresentation_types[intro.thisN]
    
    circles = [circlep0, circlep1, circlep2, circlep3, circlep4, circlep5,
               circlep6, circlep7, circlep8]
    scale = trialpresentation_levels[intro.thisN]
    sizes = [max_size] + [int(max(1, min(1.5*scale*size, max_size-1))) for size in size_pattern]
    np.random.shuffle(sizes)
    for i, (circle, size) in enumerate(zip(circles, sizes)):
        circle.size = [2 * size, 2 * size]
        circle.units = circle_units
        circle.pos = circle_positions[i]
        circle.pos[0] += randint(-min_dist / 2, min_dist / 2)
        circle.pos[1] += randint(-min_dist / 2, min_dist / 2)
        if size == max_size:
            target_circle = i
    
    # setup some python lists for storing info about the mouse_2
    gotValidClick = False  # until a click is received
    mouse_2.mouseClock.reset()
    # keep track of which components have finished
    trialpresentationComponents = [circlep0, circlep1, circlep2, circlep3, circlep4, circlep5, circlep6, circlep7, circlep8, mouse_2, ISI_2]
    for thisComponent in trialpresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialpresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialpresentation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialpresentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialpresentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circlep0* updates
        if circlep0.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep0.frameNStart = frameN  # exact frame index
            circlep0.tStart = t  # local t and not account for scr refresh
            circlep0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep0, 'tStartRefresh')  # time at next scr refresh
            circlep0.setAutoDraw(True)
        if circlep0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep0.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep0.tStop = t  # not accounting for scr refresh
                circlep0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep0, 'tStopRefresh')  # time at next scr refresh
                circlep0.setAutoDraw(False)
        
        # *circlep1* updates
        if circlep1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep1.frameNStart = frameN  # exact frame index
            circlep1.tStart = t  # local t and not account for scr refresh
            circlep1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep1, 'tStartRefresh')  # time at next scr refresh
            circlep1.setAutoDraw(True)
        if circlep1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep1.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep1.tStop = t  # not accounting for scr refresh
                circlep1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep1, 'tStopRefresh')  # time at next scr refresh
                circlep1.setAutoDraw(False)
        
        # *circlep2* updates
        if circlep2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep2.frameNStart = frameN  # exact frame index
            circlep2.tStart = t  # local t and not account for scr refresh
            circlep2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep2, 'tStartRefresh')  # time at next scr refresh
            circlep2.setAutoDraw(True)
        if circlep2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep2.tStop = t  # not accounting for scr refresh
                circlep2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep2, 'tStopRefresh')  # time at next scr refresh
                circlep2.setAutoDraw(False)
        
        # *circlep3* updates
        if circlep3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep3.frameNStart = frameN  # exact frame index
            circlep3.tStart = t  # local t and not account for scr refresh
            circlep3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep3, 'tStartRefresh')  # time at next scr refresh
            circlep3.setAutoDraw(True)
        if circlep3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep3.tStop = t  # not accounting for scr refresh
                circlep3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep3, 'tStopRefresh')  # time at next scr refresh
                circlep3.setAutoDraw(False)
        
        # *circlep4* updates
        if circlep4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep4.frameNStart = frameN  # exact frame index
            circlep4.tStart = t  # local t and not account for scr refresh
            circlep4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep4, 'tStartRefresh')  # time at next scr refresh
            circlep4.setAutoDraw(True)
        if circlep4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep4.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep4.tStop = t  # not accounting for scr refresh
                circlep4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep4, 'tStopRefresh')  # time at next scr refresh
                circlep4.setAutoDraw(False)
        
        # *circlep5* updates
        if circlep5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep5.frameNStart = frameN  # exact frame index
            circlep5.tStart = t  # local t and not account for scr refresh
            circlep5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep5, 'tStartRefresh')  # time at next scr refresh
            circlep5.setAutoDraw(True)
        if circlep5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep5.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep5.tStop = t  # not accounting for scr refresh
                circlep5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep5, 'tStopRefresh')  # time at next scr refresh
                circlep5.setAutoDraw(False)
        
        # *circlep6* updates
        if circlep6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep6.frameNStart = frameN  # exact frame index
            circlep6.tStart = t  # local t and not account for scr refresh
            circlep6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep6, 'tStartRefresh')  # time at next scr refresh
            circlep6.setAutoDraw(True)
        if circlep6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep6.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep6.tStop = t  # not accounting for scr refresh
                circlep6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep6, 'tStopRefresh')  # time at next scr refresh
                circlep6.setAutoDraw(False)
        
        # *circlep7* updates
        if circlep7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep7.frameNStart = frameN  # exact frame index
            circlep7.tStart = t  # local t and not account for scr refresh
            circlep7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep7, 'tStartRefresh')  # time at next scr refresh
            circlep7.setAutoDraw(True)
        if circlep7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep7.tStop = t  # not accounting for scr refresh
                circlep7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep7, 'tStopRefresh')  # time at next scr refresh
                circlep7.setAutoDraw(False)
        
        # *circlep8* updates
        if circlep8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circlep8.frameNStart = frameN  # exact frame index
            circlep8.tStart = t  # local t and not account for scr refresh
            circlep8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circlep8, 'tStartRefresh')  # time at next scr refresh
            circlep8.setAutoDraw(True)
        if circlep8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circlep8.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circlep8.tStop = t  # not accounting for scr refresh
                circlep8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circlep8, 'tStopRefresh')  # time at next scr refresh
                circlep8.setAutoDraw(False)
        if t > 0.5:
            for i, circle in enumerate(circles):
                if mouse.isPressedIn(circle):
                    response = i
                    continueRoutine = False
                    responsertpres=t
        
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                mouse_2.tStop = t  # not accounting for scr refresh
                mouse_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_2, 'tStopRefresh')  # time at next scr refresh
                mouse_2.status = FINISHED
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False        # *ISI_2* period
        if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.tStart = t  # local t and not account for scr refresh
            ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
            ISI_2.start(0.5)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
            ISI_2.tStop = ISI_2.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialpresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialpresentation"-------
    for thisComponent in trialpresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    intro.addData('circlep0.started', circlep0.tStartRefresh)
    intro.addData('circlep0.stopped', circlep0.tStopRefresh)
    intro.addData('circlep1.started', circlep1.tStartRefresh)
    intro.addData('circlep1.stopped', circlep1.tStopRefresh)
    intro.addData('circlep2.started', circlep2.tStartRefresh)
    intro.addData('circlep2.stopped', circlep2.tStopRefresh)
    intro.addData('circlep3.started', circlep3.tStartRefresh)
    intro.addData('circlep3.stopped', circlep3.tStopRefresh)
    intro.addData('circlep4.started', circlep4.tStartRefresh)
    intro.addData('circlep4.stopped', circlep4.tStopRefresh)
    intro.addData('circlep5.started', circlep5.tStartRefresh)
    intro.addData('circlep5.stopped', circlep5.tStopRefresh)
    intro.addData('circlep6.started', circlep6.tStartRefresh)
    intro.addData('circlep6.stopped', circlep6.tStopRefresh)
    intro.addData('circlep7.started', circlep7.tStartRefresh)
    intro.addData('circlep7.stopped', circlep7.tStopRefresh)
    intro.addData('circlep8.started', circlep8.tStartRefresh)
    intro.addData('circlep8.stopped', circlep8.tStopRefresh)
    correctAns = target_circle == response
    # store data for intro (TrialHandler)
    intro.addData('mouse_2.started', mouse_2.tStart)
    intro.addData('mouse_2.stopped', mouse_2.tStop)
    intro.addData('ISI_2.started', ISI_2.tStart)
    intro.addData('ISI_2.stopped', ISI_2.tStop)
    
    # ------Prepare to start Routine "sliderpres"-------
    continueRoutine = True
    # update component parameters for each repeat
    rating_2.reset()
    # keep track of which components have finished
    sliderpresComponents = [rating_2, slider_3]
    for thisComponent in sliderpresComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sliderpresClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sliderpres"-------
    while continueRoutine:
        # get current time
        t = sliderpresClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sliderpresClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating_2* updates
        if rating_2.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            rating_2.frameNStart = frameN  # exact frame index
            rating_2.tStart = t  # local t and not account for scr refresh
            rating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_2, 'tStartRefresh')  # time at next scr refresh
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse  # a response ends the trial
        if 'sliderpres' not in trialpresentation_types[intro.thisN]:
            continueRoutine = False
        
        # *slider_3* updates
        if slider_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            slider_3.frameNStart = frameN  # exact frame index
            slider_3.tStart = t  # local t and not account for scr refresh
            slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
            slider_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sliderpresComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sliderpres"-------
    for thisComponent in sliderpresComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    intro.addData('rating_2.started', rating_2.tStart)
    intro.addData('rating_2.stopped', rating_2.tStop)
    intro.addData('slider_3.started', slider_3.tStartRefresh)
    intro.addData('slider_3.stopped', slider_3.tStopRefresh)
    # the Routine "sliderpres" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "wagerpres"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    gotValidClick = False  # until a click is received
    mouse_3.mouseClock.reset()
    wagerpres = np.nan
    wagerpresrt = np.nan
    # keep track of which components have finished
    wagerpresComponents = [mouse_3, betbutton, surebutton]
    for thisComponent in wagerpresComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wagerpresClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wagerpres"-------
    while continueRoutine:
        # get current time
        t = wagerpresClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wagerpresClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                mouse_3.tStop = t  # not accounting for scr refresh
                mouse_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_3, 'tStopRefresh')  # time at next scr refresh
                mouse_3.status = FINISHED
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False        if 'wagerpres' not in trialpresentation_types[intro.thisN]:
            continueRoutine = False
        if t > 0.5:
            if mouse_3.isPressedIn(bet_button):
                wagerpres = 1
                continueRoutine = False
                wagerpresrt = t
            if mouse_3.isPressedIn(sure_button):
                wagerpres = 0
                continueRoutine = False
                wagerpresrt = t
        
        
        # *betbutton* updates
        if betbutton.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            betbutton.frameNStart = frameN  # exact frame index
            betbutton.tStart = t  # local t and not account for scr refresh
            betbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(betbutton, 'tStartRefresh')  # time at next scr refresh
            betbutton.setAutoDraw(True)
        
        # *surebutton* updates
        if surebutton.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            surebutton.frameNStart = frameN  # exact frame index
            surebutton.tStart = t  # local t and not account for scr refresh
            surebutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(surebutton, 'tStartRefresh')  # time at next scr refresh
            surebutton.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wagerpresComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wagerpres"-------
    for thisComponent in wagerpresComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for intro (TrialHandler)
    intro.addData('mouse_3.started', mouse_3.tStart)
    intro.addData('mouse_3.stopped', mouse_3.tStop)
    if 'wagerpres' in trialpresentation_types[intro.thisN]:
        if wagerpres==1 and correctAns:
            score += 3
        elif wagerpres==1 and not correctAns:
            score -= 3
            score = max(0, score)
        elif not wagerpres==1:
            score += 1
    
    
    for i, wcircle in enumerate(wager_circles):
        if i<score:
            wcircle.fillColor = [1, -1, -1]
        else:
            wcircle.fillColor = [0, 0, 0]
    win.flip()
    #core.wait(3)
    #for i, wcircle in enumerate(wager_circles):
    #    wcircle.setAutoDraw(False)
    intro.addData('betbutton.started', betbutton.tStartRefresh)
    intro.addData('betbutton.stopped', betbutton.tStopRefresh)
    intro.addData('surebutton.started', surebutton.tStartRefresh)
    intro.addData('surebutton.stopped', surebutton.tStopRefresh)
    # the Routine "wagerpres" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 5 repeats of 'intro'


# ------Prepare to start Routine "Start_2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
Start_2Components = [Start]
for thisComponent in Start_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Start_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Start* updates
    if Start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Start.frameNStart = frameN  # exact frame index
        Start.tStart = t  # local t and not account for scr refresh
        Start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Start, 'tStartRefresh')  # time at next scr refresh
        Start.setAutoDraw(True)
    if Start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Start.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Start.tStop = t  # not accounting for scr refresh
            Start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Start, 'tStopRefresh')  # time at next scr refresh
            Start.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_2"-------
for thisComponent in Start_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Start.started', Start.tStartRefresh)
thisExp.addData('Start.stopped', Start.tStopRefresh)

# --------Prepare to start Staircase "trials" --------
# set up handler to look after next chosen value etc
trials = data.StairHandler(startVal=0.3, extraInfo=expInfo,
    stepSizes=[0.1, 0.05, 0.05, 0.01], stepType='lin',
    nReversals=0, nTrials=50, 
    nUp=1, nDown=3,
    minVal=0, maxVal=1,
    originPath=-1, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
level = thisTrial = 0.3  # initialise some vals

for thisTrial in trials:
    currentLoop = trials
    level = thisTrial
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(10.500000)
    # update component parameters for each repeat
    trial_type = trial_types[trials.thisTrialN % len(trial_types)]
    
    circles = [circle0, circle1, circle2, circle3, circle4, circle5,
               circle6, circle7, circle8]
    if 'easy' in trial_type:
        level = 0.9
    if 'hard' in trial_type:
        level = 0.1
    scale = 1 - level
    sizes = [max_size] + [int(max(1, min(1.5*scale*size, max_size-1))) for size in size_pattern]
    np.random.shuffle(sizes)
    for i, (circle, size) in enumerate(zip(circles, sizes)):
        circle.size = [2 * size, 2 * size]
        circle.units = circle_units
        circle.pos = circle_positions[i]
        circle.pos[0] += randint(-min_dist / 2, min_dist / 2)
        circle.pos[1] += randint(-min_dist / 2, min_dist / 2)
        if size == max_size:
            target_circle = i
    response = -1
    
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    trialComponents = [ISI, circle0, circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, mouse]
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
        
        # *circle0* updates
        if circle0.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle0.frameNStart = frameN  # exact frame index
            circle0.tStart = t  # local t and not account for scr refresh
            circle0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle0, 'tStartRefresh')  # time at next scr refresh
            circle0.setAutoDraw(True)
        if circle0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle0.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle0.tStop = t  # not accounting for scr refresh
                circle0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle0, 'tStopRefresh')  # time at next scr refresh
                circle0.setAutoDraw(False)
        
        # *circle1* updates
        if circle1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle1.frameNStart = frameN  # exact frame index
            circle1.tStart = t  # local t and not account for scr refresh
            circle1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle1, 'tStartRefresh')  # time at next scr refresh
            circle1.setAutoDraw(True)
        if circle1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle1.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle1.tStop = t  # not accounting for scr refresh
                circle1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle1, 'tStopRefresh')  # time at next scr refresh
                circle1.setAutoDraw(False)
        
        # *circle2* updates
        if circle2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle2.frameNStart = frameN  # exact frame index
            circle2.tStart = t  # local t and not account for scr refresh
            circle2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle2, 'tStartRefresh')  # time at next scr refresh
            circle2.setAutoDraw(True)
        if circle2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle2.tStop = t  # not accounting for scr refresh
                circle2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle2, 'tStopRefresh')  # time at next scr refresh
                circle2.setAutoDraw(False)
        
        # *circle3* updates
        if circle3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle3.frameNStart = frameN  # exact frame index
            circle3.tStart = t  # local t and not account for scr refresh
            circle3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle3, 'tStartRefresh')  # time at next scr refresh
            circle3.setAutoDraw(True)
        if circle3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle3.tStop = t  # not accounting for scr refresh
                circle3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle3, 'tStopRefresh')  # time at next scr refresh
                circle3.setAutoDraw(False)
        
        # *circle4* updates
        if circle4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle4.frameNStart = frameN  # exact frame index
            circle4.tStart = t  # local t and not account for scr refresh
            circle4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle4, 'tStartRefresh')  # time at next scr refresh
            circle4.setAutoDraw(True)
        if circle4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle4.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle4.tStop = t  # not accounting for scr refresh
                circle4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle4, 'tStopRefresh')  # time at next scr refresh
                circle4.setAutoDraw(False)
        
        # *circle5* updates
        if circle5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle5.frameNStart = frameN  # exact frame index
            circle5.tStart = t  # local t and not account for scr refresh
            circle5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle5, 'tStartRefresh')  # time at next scr refresh
            circle5.setAutoDraw(True)
        if circle5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle5.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle5.tStop = t  # not accounting for scr refresh
                circle5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle5, 'tStopRefresh')  # time at next scr refresh
                circle5.setAutoDraw(False)
        
        # *circle6* updates
        if circle6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle6.frameNStart = frameN  # exact frame index
            circle6.tStart = t  # local t and not account for scr refresh
            circle6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle6, 'tStartRefresh')  # time at next scr refresh
            circle6.setAutoDraw(True)
        if circle6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle6.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle6.tStop = t  # not accounting for scr refresh
                circle6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle6, 'tStopRefresh')  # time at next scr refresh
                circle6.setAutoDraw(False)
        
        # *circle7* updates
        if circle7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle7.frameNStart = frameN  # exact frame index
            circle7.tStart = t  # local t and not account for scr refresh
            circle7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle7, 'tStartRefresh')  # time at next scr refresh
            circle7.setAutoDraw(True)
        if circle7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle7.tStop = t  # not accounting for scr refresh
                circle7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle7, 'tStopRefresh')  # time at next scr refresh
                circle7.setAutoDraw(False)
        
        # *circle8* updates
        if circle8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            circle8.frameNStart = frameN  # exact frame index
            circle8.tStart = t  # local t and not account for scr refresh
            circle8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle8, 'tStartRefresh')  # time at next scr refresh
            circle8.setAutoDraw(True)
        if circle8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle8.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                circle8.tStop = t  # not accounting for scr refresh
                circle8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle8, 'tStopRefresh')  # time at next scr refresh
                circle8.setAutoDraw(False)
        if t > 0.5:
            for i, circle in enumerate(circles):
                if mouse.isPressedIn(circle):
                    response = i
                    continueRoutine = False
                    responsert = t
        
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.5  # record stop time
        
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
    trials.addOtherData('ISI.started', ISI.tStart)
    trials.addOtherData('ISI.stopped', ISI.tStop)
    trials.addOtherData('circle0.started', circle0.tStartRefresh)
    trials.addOtherData('circle0.stopped', circle0.tStopRefresh)
    trials.addOtherData('circle1.started', circle1.tStartRefresh)
    trials.addOtherData('circle1.stopped', circle1.tStopRefresh)
    trials.addOtherData('circle2.started', circle2.tStartRefresh)
    trials.addOtherData('circle2.stopped', circle2.tStopRefresh)
    trials.addOtherData('circle3.started', circle3.tStartRefresh)
    trials.addOtherData('circle3.stopped', circle3.tStopRefresh)
    trials.addOtherData('circle4.started', circle4.tStartRefresh)
    trials.addOtherData('circle4.stopped', circle4.tStopRefresh)
    trials.addOtherData('circle5.started', circle5.tStartRefresh)
    trials.addOtherData('circle5.stopped', circle5.tStopRefresh)
    trials.addOtherData('circle6.started', circle6.tStartRefresh)
    trials.addOtherData('circle6.stopped', circle6.tStopRefresh)
    trials.addOtherData('circle7.started', circle7.tStartRefresh)
    trials.addOtherData('circle7.stopped', circle7.tStopRefresh)
    trials.addOtherData('circle8.started', circle8.tStartRefresh)
    trials.addOtherData('circle8.stopped', circle8.tStopRefresh)
    correctAns = target_circle == response
    trials.addResponse(correctAns, level)
    trials.addOtherData('Response', correctAns)
    trials.addOtherData('Target', target_circle)
    for i, size in enumerate(sizes):
        trials.addOtherData('c'+str(i), size)
    trials.addOtherData('circle_response', response)
    trials.addOtherData('Scale', scale)
    trials.addOtherData('Intensity', level)
    trials.addOtherData('TrialType', trial_type)
    signal = np.log(sorted(sizes)[-1] / sorted(sizes)[-2])
    trials.addOtherData('Signal', signal)
    trials.addOtherData('Treatment', treatment)
    trials.addOtherData('cmax', sorted(sizes)[-1])
    trials.addOtherData('cmax2', sorted(sizes)[-2])
    trials.addOtherData('Trial', trials.thisTrialN)
    trials.addOtherData('Response RT', responsert)
    # NB PsychoPy doesn't handle a 'correct answer' for mouse events so doesn't know how to handle mouse with StairHandler
    trials.addOtherData('mouse.started', mouse.tStart)
    trials.addOtherData('mouse.stopped', mouse.tStop)
    
    # ------Prepare to start Routine "slider"-------
    continueRoutine = True
    # update component parameters for each repeat
    rating.reset()
    # keep track of which components have finished
    sliderComponents = [rating, image_2]
    for thisComponent in sliderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sliderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "slider"-------
    while continueRoutine:
        # get current time
        t = sliderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sliderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating* updates
        if rating.status == NOT_STARTED and 'slider' in trial_type:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        if 'slider' not in trial_type:
            continueRoutine = False
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sliderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "slider"-------
    for thisComponent in sliderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # NB PsychoPy doesn't handle a 'correct answer' for ratingscale events so doesn't know what to tell a StairHandler (or QuestHandler)
    trials.addOtherData('rating.started', rating.tStart)
    trials.addOtherData('rating.stopped', rating.tStop)
    if 'slider' in trial_types[trials.thisTrialN]:
        trials.addOtherData('Confidence', rating.getRating())
        trials.addOtherData('Confidence RT', rating.getRT())
    else:
        trials.addOtherData('Confidence', np.nan)
        trials.addOtherData('Confidence RT', np.nan)
    
    trials.addOtherData('image_2.started', image_2.tStartRefresh)
    trials.addOtherData('image_2.stopped', image_2.tStopRefresh)
    # the Routine "slider" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "wager"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_wager
    gotValidClick = False  # until a click is received
    mouse_wager.mouseClock.reset()
    wager = np.nan
    wagerrt = np.nan
    
    # keep track of which components have finished
    wagerComponents = [mouse_wager, bet_button, sure_button]
    for thisComponent in wagerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wagerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wager"-------
    while continueRoutine:
        # get current time
        t = wagerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wagerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if 'wager' not in trial_type:
            continueRoutine = False
        if t > 0.5:
            if mouse_wager.isPressedIn(bet_button):
                wager = 1
                continueRoutine = False
                wagerrt = t
            if mouse_wager.isPressedIn(sure_button):
                wager = 0
                continueRoutine = False
                wagerrt = t
        
        #for wcircle in wager_circles:
        #    if t >= 0.5 and wcircle.status == NOT_STARTED:
        #        # keep track of start time/frame for later
        #        wcircle.tStart = t  # underestimates by a little under one frame
        #        wcircle.frameNStart = frameN  # exact frame index
        #        wcircle.setAutoDraw(True)
        
        # *bet_button* updates
        if bet_button.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            bet_button.frameNStart = frameN  # exact frame index
            bet_button.tStart = t  # local t and not account for scr refresh
            bet_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bet_button, 'tStartRefresh')  # time at next scr refresh
            bet_button.setAutoDraw(True)
        
        # *sure_button* updates
        if sure_button.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            sure_button.frameNStart = frameN  # exact frame index
            sure_button.tStart = t  # local t and not account for scr refresh
            sure_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sure_button, 'tStartRefresh')  # time at next scr refresh
            sure_button.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wagerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wager"-------
    for thisComponent in wagerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # NB PsychoPy doesn't handle a 'correct answer' for mouse events so doesn't know how to handle mouse with StairHandler
    trials.addOtherData('mouse_wager.started', mouse_wager.tStart)
    trials.addOtherData('mouse_wager.stopped', mouse_wager.tStop)
    trials.addOtherData('Wager', wager)
    trials.addOtherData('Wager RT', wagerrt)
    if 'wager' in trial_types[trials.thisTrialN]:
        if wager==1 and correctAns:
            score += 3
        elif wager==1 and not correctAns:
            score -= 3
            score = max(0, score)
        elif not wager==1:
            score += 1
    trials.addOtherData('Score', score)
    
    for i, wcircle in enumerate(wager_circles):
        if i<score:
            wcircle.fillColor = [1, -1, -1]
        else:
            wcircle.fillColor = [0, 0, 0]
    win.flip()
    #core.wait(3)
    #for i, wcircle in enumerate(wager_circles):
    #    wcircle.setAutoDraw(False)
    
    trials.addOtherData('bet_button.started', bet_button.tStartRefresh)
    trials.addOtherData('bet_button.stopped', bet_button.tStopRefresh)
    trials.addOtherData('sure_button.started', sure_button.tStartRefresh)
    trials.addOtherData('sure_button.stopped', sure_button.tStopRefresh)
    # the Routine "wager" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pass_level"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pass_levelComponents = [image]
    for thisComponent in pass_levelComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pass_levelClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pass_level"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pass_levelClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pass_levelClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if score < points_to_pass_level:
            continueRoutine = False
        
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 3.0-frameTolerance:
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
        for thisComponent in pass_levelComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pass_level"-------
    for thisComponent in pass_levelComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if score >= points_to_pass_level:
        score = score % points_to_pass_level
    for i, wcircle in enumerate(wager_circles):
        if i<score:
            wcircle.fillColor = [1, -1, -1]
        else:
            wcircle.fillColor = [0, 0, 0]
    win.flip()
    
    trials.addOtherData('image.started', image.tStartRefresh)
    trials.addOtherData('image.stopped', image.tStopRefresh)
    thisExp.nextEntry()
    
# staircase completed


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [image_4]
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
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
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
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)

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
