from tkinter import *
from tkinter import ttk

## Define control methods ##

def onReset():
    print("Reset button invoked.")

############################

## Define Primary GUI container
root = Tk(className="TicTacToe")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

## Define Frames
mainFrame = ttk.Frame(root)
mainFrame.grid(row=0, column=0, sticky="N E W S")
#for i in range(0,2): mainFrame.columnconfigure(i, weight=1);
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)

labelExample = ttk.Label(mainFrame, text="Test Label")
labelExample.grid(sticky="NESW")

root.mainloop()