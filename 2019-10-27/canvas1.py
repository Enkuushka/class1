from tkinter import *

window = Tk()

canvas = Canvas(window)
canvas.grid(row=0, column = 0, sticky="news")

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
canvas.create_line(10, 0, 10, 800)
# EHLEL
for x in range(0, 500, 10):
    canvas.create_line(x, 0, x, 0)

for y in range(0, 500, 10):
    canvas.create_line(x, 0, x, 0)
# DUUSAH


window.mainloop()