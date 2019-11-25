from tkinter import *
from tkinter import ttk

def toggleCombo():
    # Using .state and .instate requires putting the state arguments
    # in some sequence data type.
    if myComboBox.instate(('readonly',)):
        myComboBox.state(("!readonly",))
        print(myComboBox.state())
    else:
        myComboBox.state(("readonly",))
        print(myComboBox.state())

def toggleDisable():
    if myComboBox.instate(('disabled',)):
        myComboBox.state(('!disabled',))
        print(myComboBox.state())
    else:
        myComboBox.state(('disabled',))
        print(myComboBox.state())

root = Tk()
root.columnconfigure(0,minsize=100, weight=1)
root.rowconfigure(0,minsize=100, weight=1)

mainFrame = ttk.Frame(root)
mainFrame.grid(row=0,column=0, sticky="N W S E")

myComboBoxVar = StringVar()
myComboBoxOptions = ["Alpha","Beta","Gamma"]
myComboBox = ttk.Combobox(mainFrame, textvariable=myComboBoxVar, values=myComboBoxOptions)
myComboBox.grid(row=0,column=0,columnspan=2)

toggleComboBoxInput = ttk.Button(mainFrame, text="toggle exclusive use of combobox predefined vals", command=toggleCombo)
toggleComboBoxInput.grid(row=1,column=0)

toggleComboBoxDisable = ttk.Button(mainFrame, text="toggle disable combobox", command=toggleDisable)
toggleComboBoxDisable.grid(row=1,column=1)

root.mainloop()