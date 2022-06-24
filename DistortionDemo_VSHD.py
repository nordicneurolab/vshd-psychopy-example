# Barrel distortion adjustment example for the NordicNeuroLab VisualSystemHD
# in-scanner display.

# Ensure that the VSHD headset display output is configured in
# extended desktop mode (eg. nVidia Surround).



from psychopy import visual, event, core  # visual imported, even if not used!
import numpy as np


# Create a VSHD window. Multisampling is enabled to reduce artifacts around
# edge of distorted image.
win = visual.VisualSystemHD(fullscr=True, screen=0, multiSample=True, numSamples=16)

# create checkerboard texture using numpy
cbTex = np.tile([[0.5, -0.5], [-0.5, 0.5]], reps=(10, 10))

# convert texture to ImageStim, make it span the whole display
cbImg = visual.ImageStim(win, image=cbTex, units='norm', size=(2, 2))

# Current value of the distortion coefficient to display
msgText = 'Distortion Coef.: {}'.format(win.distCoef)

# text to show the current distortion value
distText = visual.TextStim(win, text=msgText)

# register 'q' key to exit the app
event.globalKeys.add('q', func=core.quit)

# main loop, exits on pressing 'q'
while 1:
    # update the distortion coefficient text
    distText.text = 'Distortion Coef.: {:.3f}'.format(win.distCoef)

    # draw the checkerboard to each eye
    for eye in ('left', 'right'):
        win.setBuffer(eye)
        cbImg.draw()
        distText.draw()

    # Check if keys have been pressed to update the distortion coefficient
    if event.getKeys(['w']):
        win.distCoef += 0.001
        msgText = 'Distortion Coef.: {:.3f}'.format(win.distCoef)
    elif event.getKeys(['s']):
        win.distCoef -= 0.001
        msgText = 'Distortion Coef.: {:.3f}'.format(win.distCoef)

    win.flip()
