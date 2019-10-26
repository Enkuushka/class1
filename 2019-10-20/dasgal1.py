from tkinter import *
from tkinter import messagebox

username = "admin"
password = "123"

def checkLogin():
    if(usernameVar.get() == username and passwordVar.get() == password):
        messagebox.showinfo("Амжилттай", "Login success!")
    else:
        messagebox.showerror("Алдаа", "Login error!")

window = Tk()

usernameVar = StringVar()
passwordVar = StringVar()

window.geometry("400x300")
window.resizable(FALSE,FALSE)

frame1 = Frame(window)
frame2 = Frame(window)
loginBtn = Button(window, text="Login", command=checkLogin)

lbl1 = Label(frame1, text="Name:", width=15)
entry1 = Entry(frame1, textvariable=usernameVar)

lbl2 = Label(frame2, text="Password: ", width=15)
entry2 = Entry(frame2, show="*", textvariable=passwordVar)

lbl1.pack(side = LEFT)
entry1.pack(side = RIGHT)

lbl2.pack(side = LEFT)
entry2.pack(side = RIGHT)

frame1.pack(side=TOP)
frame2.pack(side=TOP)
loginBtn.pack(side=TOP)

window.mainloop()