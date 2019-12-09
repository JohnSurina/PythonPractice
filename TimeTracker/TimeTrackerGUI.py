from . import trackerControl
import tkinter
from tkinter import ttk
from math import trunc

def update():
    timeDelta = mTracker.timeDeltaCurrent()
    timeDeltaSeconds = timeDelta.total_seconds()

    timeDeltaHours = trunc(timeDeltaSeconds // 3600)
    remainder = timeDeltaSeconds % 3600

    timeDeltaMinutes = trunc(remainder//60)

    timeDeltaSeconds = trunc(timeDeltaSeconds - ( timeDeltaHours * 3600 + timeDeltaMinutes * 60 ))
    
    timeDeltaFormatted = 'Time since start time\nHr: {0}\nMin: {1}\nSec: {2}'.format(timeDeltaHours, timeDeltaMinutes, timeDeltaSeconds)
    time.set(timeDeltaFormatted)

    root.after(1000, func=update) # continue updating

def setTime():
    mTracker.createStartPoint()

# Set up the tracker object
mTracker = trackerControl.trackerControl()

# configure TK root
root = tkinter.Tk()
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

root.wm_title('Time Tracker')
root.after(1000, func=update) ## start automatic update

# Create reference variables
time = tkinter.StringVar(root)

# Create widgets
mainFrame = ttk.Frame(root)
mainFrame.grid(column=0, row=0, sticky='NWSE')

label = ttk.Label(mainFrame, textvariable = time)
label.grid(column=0, row=0)

resetTimeButton = ttk.Button(mainFrame, text='set initial time', command=setTime)
resetTimeButton.grid(column=0, row = 1)

update()
root.mainloop