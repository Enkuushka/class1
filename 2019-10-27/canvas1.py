from tkinter import *
from tkinter import ttk

def addLine():
    global window
    topLevel = Toplevel(window)
    label1 = Label(topLevel, text="X1")
    label2 = Label(topLevel, text="Y1")
    label3 = Label(topLevel, text="X2")
    label4 = Label(topLevel, text="Y2")

window = Tk()

h = ttk.Scrollbar(window, orient=HORIZONTAL)
v = ttk.Scrollbar(window, orient=VERTICAL)

lineButton = Button(window, text="Line...", command=addLine)

canvas = Canvas(window, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview


lineButton.grid(column=0, row=0)
ttk.Sizegrip(window).grid(column=1, row=2, sticky=(S,E))
canvas.grid(column=0, row=1, sticky=(N,W,E,S))
h.grid(column=0, row=2, sticky=(W,E))
v.grid(column=1, row=1, sticky=(N,S))
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

# Шулуун зурах     x1  y1  x2   y2
shape_Id1 = canvas.create_line(10, 10, 150, 300)

# дүрсийн шинж чанарыг өөрчлөх
canvas.itemconfigure(shape_Id1, fill='red', width=3)

canvas.create_arc((0, 0, 80, 80), fill='green')

canvas.create_oval(100, 100, 150, 150)

canvas.create_rectangle(100, 100, 200, 150)

canvas.create_polygon(100, 100, 200, 340, 340, 230, 140, 250)

# 500 x 500
canvas.create_line(0, 10, 500, 10)
canvas.create_line(10, 0, 10, 500)

for x in range(0, 500, 100):
    canvas.create_line(x, 0, x, 10)
    canvas.create_text(x, 20, text=str(x))

for y in range(0, 500, 100):
    canvas.create_line(0, y, 10, y)
    canvas.create_text(20, y, text=str(y))

theImage = PhotoImage(file='D:/class1/2019-10-27/google_logo.png')

canvas.create_image(272, 92, image=theImage)


window.mainloop()