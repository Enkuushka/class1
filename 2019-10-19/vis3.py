from tkinter import *
from tkinter import ttk

window = Tk()

myValues = ("AAA", "BBB", "CCC")
myVar = StringVar()

cbox = ttk.Combobox(window, values=myValues)
cbox.pack()


listbox = ["11", "22", "33"]
listVars =  StringVar(value=listbox)
lbox = Listbox(window, listvariable=listVars)
lbox.pack()

window.mainloop()