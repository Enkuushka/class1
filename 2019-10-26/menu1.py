from tkinter import *

def openFile():
    print("will open file.")

window = Tk()

menubar = Menu(window)
fileMenu = Menu(menubar)
editMenu = Menu(menubar)
menubar.add_cascade(menu=fileMenu, label="FiLe")
menubar.add_cascade(menu=editMenu, label="EdiT")

fileMenu.add_command(label="Open...", command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

check = StringVar()
editMenu.add_checkbutton(label='Check', variable=check, onvalue=1, offvalue=0)
editMenu.add_separator()

radio = StringVar()
editMenu.add_radiobutton(label='One', variable=radio, value=1)
editMenu.add_radiobutton(label='Two', variable=radio, value=2)
editMenu.add_radiobutton(label='Three', variable=radio, value=3)

fileMenu.entryconfigure('Exit', state=DISABLED)

window["menu"] = menubar

window.mainloop()