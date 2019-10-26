from tkinter import *

window = Tk()

floatValue = 2.33333333333
strValue = "%.2f C" % (floatValue)
print(strValue)

def metricChanged():
    print("OK"+measureSystem.get())

measureSystem = StringVar()
check = Checkbutton(window, text='Temperature unit is Celsius', 
	    command=metricChanged, variable=measureSystem,
	    onvalue='celsius', offvalue='farenheit')


frame1 = Frame(window, relief="raised", borderwidth=2)
phone = StringVar()
home = Radiobutton(frame1, text='Home', variable=phone, value='home')
office = Radiobutton(frame1, text='Office', variable=phone, value='office')
cell = Radiobutton(frame1, text='Mobile', variable=phone, value='cell')

phone.set('none')

frame2 = Frame(window, relief="groove", borderwidth=5)
mail = StringVar()
home1 = Radiobutton(frame2, text='Home', variable=mail, value='home')
office1 = Radiobutton(frame2, text='Office', variable=mail, value='office')
mail.set('home')

check.pack()



home.pack()
office.pack()
cell.pack()

home1.pack()
office1.pack()


frame1.pack()
frame2.pack()



window.mainloop()