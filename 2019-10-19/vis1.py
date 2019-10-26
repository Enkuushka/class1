# from tkinter import *
# window = Tk()

import tkinter
window = tkinter.Tk()

birthYear = tkinter.StringVar()
output = tkinter.Text(window, width=20, height=5, wrap='none', state="disabled")

def doClick():
    output['state'] = 'normal'
    output.insert('end',"Your age: " + str(2019 - int(birthYear.get())))
    output.insert('end', '\n')
    output['state'] = 'disabled'

myLabel = tkinter.Label(window, text="Enter your birth year:")
theImage = tkinter.PhotoImage(file='google.png')
myLabel["anchor"] = "s"
myLabel["image"] = theImage
# myLabel["background"] = "blue"
# myLabel["foreground"] = "white"
# myLabel["padx"] = 10
# myLabel["pady"] = 30
myLabel.pack()

entryWidget = tkinter.Entry(window, textvariable=birthYear)
entryWidget["background"] = "green"
entryWidget["foreground"] = "yellow"
entryWidget.pack()

myButton = tkinter.Button(window, text="My button", command=doClick)
myButton["background"] = "red"
myButton["foreground"] = "yellow"
myButton.pack()
output.pack()

output["background"] = "yellow"
output["foreground"] = "brown"

window.mainloop()