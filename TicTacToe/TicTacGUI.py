import TicTacToeBoard as TTT
from tkinter import *
from tkinter import ttk


## Initialize Board ##

board = TTT.TicTacToeBoard()

## Define control methods ##

def onReset():
    print("Reset button invoked.")

def onStart():
    print("Start button invoked.")

def onSymbolUpdate(player:int):
    if player == 1:
        isAccepted = board.changeSym(1, player1SymbolText.get())
        if not isAccepted:
            player1SymbolText


############################

## Define Primary GUI container
root = Tk(className="TicTacToe")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

## Define Frames
mainFrame = ttk.Frame(root)
mainFrame.grid(row=0, column=0, sticky="N E W S")
for i in range(0,2): mainFrame.columnconfigure(i, weight=1);

gameFrame = ttk.Frame(mainFrame,padding=10)
gameFrame.grid(column=0, row=1, sticky="WE")

controlFrame = ttk.Frame(mainFrame,padding=10)
controlFrame.grid(column=1, row=1, sticky="WE")
controlFrame.columnconfigure(0, weight=1);

## Define GUI Variables and content options.
stateDescriptionPossibilities = ['Player 1\'s turn','Player 2\'s turn','Initialize game',
    'Player 1 Wins!','Player 2 Wins!','Draw']
stateDescription = StringVar(value=stateDescriptionPossibilities[2])

topLeft = StringVar(value="")
topMiddle = StringVar(value="")
topRight = StringVar(value="")
middleLeft = StringVar(value="")
middleMiddle = StringVar(value="")
middleRight = StringVar(value="")
bottomLeft = StringVar(value="")
bottomMiddle = StringVar(value="")
bottomRight = StringVar(value="")

## Define Widgets
turnTracker = ttk.Label(mainFrame, textvariable=stateDescription)
turnTracker.grid(column=0,row=0)

resetButton = ttk.Button(controlFrame, text="Reset", command=onReset)
resetButton.grid(column=0, row=0)

player1EntryFrame = ttk.Frame(controlFrame)
player1EntryFrame.grid(column=0, row=1)

player1SymbolLabel = ttk.Label(player1EntryFrame, text="Player 1 Symbol:")
player1SymbolLabel.grid(column=0, row=0)

player1SymbolText = ttk.Entry(player1EntryFrame)
player1SymbolText.grid(column=1, row=0)

player2EntryFrame = ttk.Frame(controlFrame)
player2EntryFrame.grid(column=0, row=2)

player2SymbolLabel = ttk.Label(player2EntryFrame, text="Player 2 Symbol:")
player2SymbolLabel.grid(column=0, row=0)

player2SymbolText = ttk.Entry(player2EntryFrame)
player2SymbolText.grid(column=1, row=0)

startButton = ttk.Button(controlFrame, text="Start", command=onStart)
startButton.grid(column=0, row=3)

incorrectSymbolLabel = ttk.Label(controlFrame, text="Please set the player symbols correctly")
incorrectSymbolLabel.grid(column=0, row=4)

    ## Define game buttons

topLeftButton = ttk.Button(gameFrame, textvariable=topLeft)
topLeftButton.grid(row=0,column=0)

topMiddleButton = ttk.Button(gameFrame, textvariable=topMiddle)
topMiddleButton.grid(row=0,column=1)

topRightButton = ttk.Button(gameFrame, textvariable=topRight)
topRightButton.grid(row=0,column=2)

middleLeftButton = ttk.Button(gameFrame, textvariable=middleLeft)
middleLeftButton.grid(row=1,column=0)

middleMiddleButton = ttk.Button(gameFrame, textvariable=middleMiddle)
middleMiddleButton.grid(row=1,column=1)

middleRightButton = ttk.Button(gameFrame, textvariable=middleRight)
middleRightButton.grid(row=1,column=2)

bottomLeftButton = ttk.Button(gameFrame, textvariable=bottomLeft)
bottomLeftButton.grid(row=2,column=0)

bottomMiddleButton = ttk.Button(gameFrame, textvariable=bottomMiddle)
bottomMiddleButton.grid(row=2,column=1)

bottomRightButton = ttk.Button(gameFrame, textvariable=bottomRight)
bottomRightButton.grid(row=2,column=2)


root.mainloop()