# VSHD 2D demo for PsychoPy taken from comments here:
# https://github.com/mdcutone/psychopy/blob/nnl-view/psychopy/visual/nnlvs.py
#
# Ensure that the VSHD headset display output is configured in
# extended desktop mode (eg. nVidia Surround).

from psychopy import visual, core, event

# Create a visual window
win = visual.VisualSystemHD(fullscr=True, screen=1)

# Initialize some stimuli, note contrast, opacity, ori
grating1 = visual.GratingStim(win, mask="circle", color='white',
    contrast=0.5, size=(1.0, 1.0), sf=(4, 0), ori = 45, autoLog=False)
grating2 = visual.GratingStim(win, mask="circle", color='white',
    opacity=0.5, size=(1.0, 1.0), sf=(4, 0), ori = -45, autoLog=False,
    pos=(0.1, 0.1))

trialClock = core.Clock()
t = 0
while not event.getKeys() and t < 20:
    t = trialClock.getTime()
    for eye in ('left', 'right'):
        win.setBuffer(eye)  # change the buffer
        grating1.phase = 1 * t  # drift at 1Hz
        grating1.draw()  # redraw it
        grating2.phase = 2 * t    # drift at 2Hz
        grating2.draw()  # redraw it

    win.flip()

win.close()
core.quit()
