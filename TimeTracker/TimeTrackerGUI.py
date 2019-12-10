from . import trackerControl
import tkinter
from tkinter import ttk
from math import trunc
from datetime import datetime

def update():
    timeDelta = mTracker.timeDeltaCurrent()
    timeDeltaSeconds = timeDelta.total_seconds()

    timeDeltaHours = trunc(timeDeltaSeconds // 3600)
    remainder = timeDeltaSeconds % 3600

    timeDeltaMinutes = trunc(remainder//60)

    timeDeltaSeconds = trunc(timeDeltaSeconds - ( timeDeltaHours * 3600 + timeDeltaMinutes * 60 ))

    timeDeltaFormatted = 'Time since start time\nHr: {0}\nMin: {1}\nSec: {2}\n\nPut in timesheet: {0}.{3}Hrs'.format(
        timeDeltaHours, timeDeltaMinutes, timeDeltaSeconds, calcTimePartial(timeDeltaMinutes))
    time.set(timeDeltaFormatted)

    root.after(1000, func=update) # continue updating

def calcTimePartial(minutes):
    if minutes<15:
        return(0)
    elif minutes<30:
        return(25)
    elif minutes<45:
        return(5)
    elif minutes<60:
        return(75)
    else:
        raise Exception()

def setTime():
    mTracker.createStartPoint()

def onOverrideButton():
    '''Toggles the Time override frame'''
    global overrideViewOpen
    if overrideViewOpen:
        overrideFrame.grid_remove()
        overrideViewOpen = False
    else:
        overrideFrame.grid()
        overrideViewOpen = True

def onOverrideStart():
    try:
        year = int(overrideYearEntry.get())
    except ValueError:
        year = datetime.now().year
    
    try:
        month = int(overrideMonthEntry.get())
    except ValueError:
        month = datetime.now().month

    try:
        day = int(overrideDayEntry.get())
    except ValueError:
        day = datetime.now().day

    try:
        hour = int(overrideHourEntry.get())
    except ValueError:
        hour = datetime.now().hour

    try:
        minute = int(overrideMinuteEntry.get())
    except ValueError:
        minute = datetime.now().minute
    
    mTracker.forceStartPoint(year,month,day,hour,minute)

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

overrideViewOpen = False

# Create widgets
mainFrame = ttk.Frame(root)
mainFrame.grid(column=0, row=0, sticky='NWSE')

label = ttk.Label(mainFrame, textvariable = time)
label.grid(column=0, row=0, sticky='W')

resetTimeButton = ttk.Button(mainFrame, text='set initial time', command=setTime)
resetTimeButton.grid(column = 0, row = 1)

overrideStartButton = ttk.Button(mainFrame, text='override start time', command=onOverrideButton)
overrideStartButton.grid(column = 0, row = 2)

overrideFrame = ttk.Frame(mainFrame)
overrideFrame.grid(column = 0, row = 3); overrideFrame.grid_remove()

overrideYearLabel = ttk.Label(overrideFrame, text = 'Yr')
overrideYearLabel.grid(row=0,column=0)

overrideMonthLabel = ttk.Label(overrideFrame, text = 'Mo')
overrideMonthLabel.grid(row=0,column=1)

overrideDayLabel = ttk.Label(overrideFrame, text = 'Day')
overrideDayLabel.grid(row=0,column=2)

overrideHourLabel = ttk.Label(overrideFrame, text = 'Hr')
overrideHourLabel.grid(row=0,column=3)

overrideMinuteLabel = ttk.Label(overrideFrame, text = 'Min')
overrideMinuteLabel.grid(row=0,column=4)

overrideYearEntry = ttk.Entry(overrideFrame, width=4)
overrideYearEntry.grid(row=1,column=0)
overrideYearEntry.bind(sequence='<Key-Return>',func=lambda e:onOverrideStart())

overrideMonthEntry = ttk.Entry(overrideFrame, width=2)
overrideMonthEntry.grid(row=1,column=1)
overrideMonthEntry.bind(sequence='<Key-Return>',func=lambda e:onOverrideStart())

overrideDayEntry = ttk.Entry(overrideFrame, width=2)
overrideDayEntry.grid(row=1,column=2)
overrideDayEntry.bind(sequence='<Key-Return>',func=lambda e:onOverrideStart())

overrideHourEntry = ttk.Entry(overrideFrame, width=2)
overrideHourEntry.grid(row=1,column=3)
overrideHourEntry.bind(sequence='<Key-Return>',func=lambda e:onOverrideStart())

overrideMinuteEntry = ttk.Entry(overrideFrame, width=2)
overrideMinuteEntry.grid(row=1,column=4)
overrideMinuteEntry.bind(sequence='<Key-Return>',func=lambda e:onOverrideStart())


update()
root.mainloop()