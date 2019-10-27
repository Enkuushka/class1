from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("600x400")

h = ttk.Scrollbar(window, orient=HORIZONTAL)
v = ttk.Scrollbar(window, orient=VERTICAL)

canvas = Canvas(window, scrollregion=(0, 0, 600, 400), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview

ttk.Sizegrip(window).grid(column=1, row=2, sticky=(S,E))
canvas.grid(column=0, row=1, sticky=(N,W,E,S))
h.grid(column=0, row=2, sticky=(W,E))
v.grid(column=1, row=1, sticky=(N,S))
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)


#
# 1. Read data from data.txt
# 2. Draw graph
#


window.mainloop()