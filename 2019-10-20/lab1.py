from tkinter import *

window = Tk()

#
# pack(...) method
#   argument names:
#   - expand "Boolean value"
#   - fill NONE, X, Y, BOTH
#   - side TOP, BOTTOM, LEFT, RIGHT

frame1 = Frame(window, borderwidth=5, relief='raised')

btn1 = Button(frame1, text="Btn 1")
btn1.pack(expand = True, fill = BOTH, side = LEFT)

btn2 = Button(frame1, text="Btn 2")
btn2.pack(side = LEFT)

frame1.pack(expand = True, fill = BOTH, side = TOP)

lbl1 = Label(window, text="Label 1")
lbl1.pack(side = BOTTOM)

window.mainloop()