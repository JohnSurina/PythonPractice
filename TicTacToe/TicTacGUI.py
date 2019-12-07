#!/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from . import TicTacToeBoard as TTT
from tkinter import *
from tkinter import ttk


## Initialize Board ##

board = TTT.TicTacToeBoard()

## Define control methods ##

def onReset():
    print("Reset button invoked.")
    for button in buttonTuple:
        button.state(['disabled'])
    resetButton.grid_remove()
    player1EntryFrame.grid()
    player2EntryFrame.grid()
    startButton.grid()
    board.resetBoard()
    synchronizeBoardModelWithViewModel()
    stateDescription.set(stateDescriptionPossibilities[2])

def onStart():
    print("Start button invoked.")
    for button in buttonTuple:
        button.state(['!disabled'])
    resetButton.grid()
    player1EntryFrame.grid_remove()
    player2EntryFrame.grid_remove()
    startButton.grid_remove()
    board.resetBoard()
    synchronizeBoardModelWithViewModel()
    stateDescription.set(stateDescriptionPossibilities[0])

def onSymbolUpdate(player:int):
    global symbol1Okay
    global symbol2Okay
    if player == 1:
        isAccepted = board.changeSym(1, player1SymbolText.get())
        if not isAccepted:
            player1SymbolText.configure(foreground='red')
            symbol1Okay = False
        else:
            player1SymbolText.configure(foreground='black')
            symbol1Okay = True
    elif player == 2:
        isAccepted = board.changeSym(2, player2SymbolText.get())
        if not isAccepted:
            player2SymbolText.configure(foreground='red')
            symbol2Okay = False
        else:
            player2SymbolText.configure(foreground='black')
            symbol2Okay = True
    adjustStartButtonState()
    adjustIncorrectSystemLabel()

def adjustStartButtonState():
    global symbol1Okay
    global symbol2Okay
    if symbol1Okay and symbol2Okay:
        startButton.state(['!disabled'])
    else:
        startButton.state(['disabled'])

def adjustIncorrectSystemLabel():
    global symbol1Okay
    global symbol2Okay
    if symbol1Okay and symbol2Okay:
        incorrectSymbolLabel.grid_remove()
    else:
        incorrectSymbolLabel.grid()

def synchronizeBoardModelWithViewModel():
    topLeft.set(board.boardVals['p13'])
    topMiddle.set(board.boardVals['p23'])
    topRight.set(board.boardVals['p33'])
    middleLeft.set(board.boardVals['p12'])
    middleMiddle.set(board.boardVals['p22'])
    middleRight.set(board.boardVals['p32'])
    bottomLeft.set(board.boardVals['p11'])
    bottomMiddle.set(board.boardVals['p21'])
    bottomRight.set(board.boardVals['p31'])

def ticTacMove(location:str):
    if stateDescription.get() == stateDescriptionPossibilities[0]:
        returnBool = board.player1move(location)
        nextState = stateDescriptionPossibilities[1]
    elif stateDescription.get() == stateDescriptionPossibilities[1]:
        returnBool = board.player2move(location)
        nextState = stateDescriptionPossibilities[0]
    else:
        print('something went wrong')
        return(False)
    
    if returnBool == False:
        incorrectMoveLabel.grid()
        return(False)
    else:
        incorrectMoveLabel.grid_remove()
        synchronizeBoardModelWithViewModel()
    
    isWon,winner = board.isWon()
    if isWon:
        if winner == 1:
            nextState = stateDescriptionPossibilities[3]
        elif winner == 2:
            nextState = stateDescriptionPossibilities[4]
        else:
            nextState = stateDescriptionPossibilities[5]
        for button in buttonTuple:
            button.state(['disabled'])
    stateDescription.set(nextState)
    return(True)

############################

## Define Primary GUI container
root = Tk()
root.title('TicTacToe')
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

## Define Frames
mainFrame = ttk.Frame(root)
mainFrame.grid(row=0, column=0, sticky="N E W S")
for i in range(0,2): mainFrame.columnconfigure(i, weight=1);

gameFrame = ttk.Frame(mainFrame,padding=10)
gameFrame.grid(column=0, row=1, sticky="NWE")

controlFrame = ttk.Frame(mainFrame,padding=10)
controlFrame.grid(column=1, row=1, sticky="WE")
controlFrame.columnconfigure(0, weight=1);

## Define GUI Variables and content options.
stateDescriptionPossibilities = ['Player 1\'s turn','Player 2\'s turn','Initialize game',
    'Player 1 Wins!','Player 2 Wins!','Draw']
stateDescription = StringVar(value=stateDescriptionPossibilities[2])

symbol1Variable = StringVar(root,value=board.p1_sym) # this does NOT 2-way bind the value, must have callback
symbol1Variable.trace_add('write', lambda a,b,c: onSymbolUpdate(1))
symbol1Okay = True # this is set true because we initially set good symbols

symbol2Variable = StringVar(root,value=board.p2_sym) # this does NOT 2-way bind the value, must have callback
symbol2Variable.trace_add('write', lambda a,b,c: onSymbolUpdate(2))
symbol2Okay = True # this is set true because we initially set good symbols

topLeft = StringVar(value="")
topMiddle = StringVar(value="")
topRight = StringVar(value="")
middleLeft = StringVar(value="")
middleMiddle = StringVar(value="")
middleRight = StringVar(value="")
bottomLeft = StringVar(value="")
bottomMiddle = StringVar(value="")
bottomRight = StringVar(value="")

################# Define Widgets
turnTracker = ttk.Label(mainFrame, textvariable=stateDescription)
turnTracker.grid(column=0,row=0)

resetButton = ttk.Button(controlFrame, text="Reset", command=onReset)
resetButton.grid(column=0, row=0)
resetButton.grid_remove() # do not show reset button while configuring

player1EntryFrame = ttk.Frame(controlFrame)
player1EntryFrame.grid(column=0, row=1)

player1SymbolLabel = ttk.Label(player1EntryFrame, text="Player 1 Symbol:")
player1SymbolLabel.grid(column=0, row=0)

player1SymbolText = ttk.Entry(player1EntryFrame, textvariable = symbol1Variable)
player1SymbolText.grid(column=1, row=0)

player2EntryFrame = ttk.Frame(controlFrame)
player2EntryFrame.grid(column=0, row=2)

player2SymbolLabel = ttk.Label(player2EntryFrame, text="Player 2 Symbol:")
player2SymbolLabel.grid(column=0, row=0)

player2SymbolText = ttk.Entry(player2EntryFrame, textvariable = symbol2Variable)
player2SymbolText.grid(column=1, row=0)

startButton = ttk.Button(controlFrame, text="Start", command=onStart)
startButton.grid(column=0, row=3)

incorrectSymbolLabel = ttk.Label(controlFrame, foreground = 'red',
    justify = 'center', text="Player symbols must be a single\nnonspace character")
incorrectSymbolLabel.grid(column=0, row=4)
incorrectSymbolLabel.grid_remove() # do not display by default

incorrectMoveLabel = ttk.Label(controlFrame, foreground = 'red',
    justify = 'center', text = "invalid move")
incorrectMoveLabel.grid(column=0, row=5)
incorrectMoveLabel.grid_remove()

    ## Define game buttons

topLeftButton = ttk.Button(gameFrame, command=lambda: ticTacMove('topleft'), textvariable=topLeft)
topLeftButton.grid(row=0,column=0)

topMiddleButton = ttk.Button(gameFrame, command=lambda: ticTacMove('topmiddle'), textvariable=topMiddle)
topMiddleButton.grid(row=0,column=1)

topRightButton = ttk.Button(gameFrame, command=lambda: ticTacMove('topright'), textvariable=topRight)
topRightButton.grid(row=0,column=2)

middleLeftButton = ttk.Button(gameFrame, command=lambda: ticTacMove('middleleft'), textvariable=middleLeft)
middleLeftButton.grid(row=1,column=0)

middleMiddleButton = ttk.Button(gameFrame, command=lambda: ticTacMove('middlemiddle'), textvariable=middleMiddle)
middleMiddleButton.grid(row=1,column=1)

middleRightButton = ttk.Button(gameFrame, command=lambda: ticTacMove('middleright'), textvariable=middleRight)
middleRightButton.grid(row=1,column=2)

bottomLeftButton = ttk.Button(gameFrame, command=lambda: ticTacMove('bottomleft'), textvariable=bottomLeft)
bottomLeftButton.grid(row=2,column=0)

bottomMiddleButton = ttk.Button(gameFrame, command=lambda: ticTacMove('bottommiddle'), textvariable=bottomMiddle)
bottomMiddleButton.grid(row=2,column=1)

bottomRightButton = ttk.Button(gameFrame, command=lambda: ticTacMove('bottomright'), textvariable=bottomRight)
bottomRightButton.grid(row=2,column=2)

buttonTuple = (topLeftButton,    topMiddleButton,    topRightButton,
               middleLeftButton, middleMiddleButton, middleRightButton,
               bottomLeftButton, bottomMiddleButton, bottomRightButton)
for button in buttonTuple:
    button.state(['disabled'])

# Run the application
root.mainloop()