from tkinter import *
from tkinter import ttk

def convertFeetToMeters():
    feet = float(feetDisplay.get())
    meters = feet*(12/1)*(.0254/1)
    metersDisplay.set(meters)


# Tk window instantiation and configuration
root = Tk(className="Meters to Feet")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# Variable Instantiation
feetDisplay = StringVar(root)
metersDisplay = StringVar(root)

# Primary content frame instantiation and configuration
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(row=0,column=0,sticky=(N,E,W,S))
frame.columnconfigure(2,weight=1)

# Define input label
inputLabel = ttk.Label(frame, text="Input: ", justify="right")
inputLabel.grid(row=1,column=0)

# Define output label
outputLabel = ttk.Label(frame, text="Output: ", justify="right")
outputLabel.grid(row=2,column=0)

# Define Feet entry field
inputEntryField = ttk.Entry(frame, width=7, textvariable=feetDisplay)
inputEntryField.grid(column=1,row=1, sticky=(E,W))

# Define Meters output field
outputField = ttk.Label(frame,textvariable=metersDisplay)
outputField.grid(row=2, column=1)

# Define Primary Header
header = ttk.Label(frame,text="Convert Feet to Meters", justify="center")
header.grid(columnspan=3,column=0,row=0,sticky=(E,W))

# Define conversion button
convertButton = ttk.Button(frame,text="Convert",command=convertFeetToMeters)
convertButton.grid(column=2,row=2)

root.mainloop()