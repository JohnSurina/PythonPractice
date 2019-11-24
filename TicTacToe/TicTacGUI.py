import TicTacToeBoard as TTT
from tkinter import *

root = Tk(className="TicTacToe")
mFrame = Frame(root).grid()

button = Button(mFrame, command = lambda:print("hello!")).grid()
button2 = Button(mFrame, command = lambda:print("goodbye!")).grid()

label = Label(root).grid

root.mainloop()