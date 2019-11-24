# First Hello world example (works)

# from tkinter import *

# root = Tk(className="Hello World!")

# frame = Frame(root)
# frame.pack()

# myStr = StringVar(root, value="Hello World!")

# label = Label(frame, textvariable=myStr).pack()

# root.mainloop()

#################################################

from tkinter import *
import tkinter.ttk

root = Tk(className="Hello World Window")
tkinter.ttk.Button(root,text="hello World").grid()
root.mainloop()
