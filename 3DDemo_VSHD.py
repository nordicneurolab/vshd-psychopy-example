#3D example for NordicNeuroLab VisualSystemHD
#This script is based on the stim3d.py demo provided with PyschoPy

# Ensure that the VSHD headset display output is configured in
# extended desktop mode (eg. nVidia Surround).

from psychopy import core
import psychopy.visual as visual
from psychopy.visual import LightSource, BlinnPhongMaterial, BoxStim
from psychopy import event

win = visual.VisualSystemHD(fullscr=True, screen = 0)   
ipd = 6.0 #Interpupillary distance in cm. Measure the users IPD for displaying 3D stimuli correctly

redLight = LightSource(win, pos=(0, 1, 0), diffuseColor=(.5, 0., 0.9,),
                       specularColor=(.5, .5, .5), lightType='directional')
blueLight = LightSource(win, pos = (5, -3, 0.), diffuseColor = (0., 0., .5),
                        specularColor=(.5, .5, .5), lightType = 'point')
greenLight = LightSource(win, pos = (-5, -3, 0.), diffuseColor=(0., .5, 0.),
                         specularColor = (.5, .5, .5), lightType='point')


# assign the lights to the scene
win.lights = [redLight, blueLight, greenLight]

# create the stimulus object, try other classes like SphereStim and PlaneStim
boxStim = BoxStim(win, size=(.2, .2, .2))

# set the position of the object by editing the associated rigid body pose
boxStim.thePose.pos = (0, 0, -3)

# create a white material and assign it
boxStim.material = BlinnPhongMaterial(win, diffuseColor=(1, 1, 1), specularColor=(0, 0, 0), shininess=125.0)

# set the box 3 meters away from the observer by editing the stimuli's rigid
# body class
boxStim.thePose.pos = (0, 0, -3)

# text to overlay
message = visual.TextStim(win, text='Any key to quit', pos=(0, -0.8), units='norm')

angle = 0.0
while not event.getKeys():

    for eye in ("left", "right"): 
        
        win.setBuffer(eye) # Change the buffer between right and left eye
        if eye == "left":
            win.eyeOffset = -ipd / 2.0
        else:
            win.eyeOffset = ipd / 2.0
        
        win.setPerspectiveView()  # set the projection, must be done every frame
        win.useLights = True  # enable lighting
        boxStim.thePose.setOriAxisAngle((0, 1, 1), angle)  # spin the stimulus by angle
        boxStim.draw()             # draw the stimulus
        win.resetEyeTransform()    # reset the transformation to draw 2D stimuli
        win.useLights = False     # disable lights for 2D stimuli, or else colors will be modulated
        message.draw()

    win.flip()

    angle += 0.5

win.close()
core.quit()

