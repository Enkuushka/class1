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
fileHandler = open("D:/class1/2019-10-27/data.txt", "r")
lineList = fileHandler.readlines()
data = []
for line in lineList:
    d = line.split("\n")[0].split(" ")
    data.append({
        "year" : int(d[0]),
        "pop" : int(d[1])
    })
fileHandler.close()


# 2. Draw graph
#
totalData = len(data)
w = 500
h = 300
canvas.create_line(100, 50, 100, 350)
canvas.create_line(100, 350, 600, 350)
x_step = int(w/totalData)

for x in range(100, 600, x_step):
    canvas.create_line(x, 350, x, 360)

max = 0
for elem in data:
    if(max < elem["pop"]):
        max = elem["pop"]

y_step = max/h
print("y_step = " + str(y_step))
counter = 0
for elem in data:
    y_value = (350 - elem["pop"] / y_step) + 150
    canvas.create_oval(100 + counter*x_step, y_value, 100 + counter*x_step + 5, y_value + 5)
    canvas.create_text(100 + counter*x_step, 360, text=str(elem["year"]))
    counter=counter+1


window.mainloop()