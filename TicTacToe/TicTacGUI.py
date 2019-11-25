import TicTacToeBoard as TTT
from tkinter import *
from tkinter import ttk

## Define control methods ##

def onReset():
    print("Reset button invoked.")

############################

## Define Primary GUI container
root = Tk(className="TicTacToe")

## Define Frames
mainFrame = ttk.Frame(root)
mainFrame.grid(sticky="NEWS")
for i in range(0,2): mainFrame.columnconfigure(i, weight=1);

gameFrame = ttk.Frame(mainFrame,padding=10)
gameFrame.grid(column=0, row=1, sticky="WE")

controlFrame = ttk.Frame(mainFrame,padding=10)
controlFrame.grid(column=1, row=1, sticky="WE")

## Define GUI Variables and content options.
whosTurnPossibilities = ['Player 1\'s turn','Player 2\'s turn']
whosTurn = StringVar()

## Define Widgets
turnTracker = ttk.Label(mainFrame, textvariable=whosTurn)
turnTracker.grid(column=0,row=0)

resetButton = ttk.Button(controlFrame, text="Reset", command=onReset)
resetButton.grid(column=1, row=0)

root.mainloop()