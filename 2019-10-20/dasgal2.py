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

lbl1 = Label(window, text="Name:", width=15)
entry1 = Entry(window, textvariable=usernameVar)

lbl2 = Label(window, text="Password: ", width=15)
entry2 = Entry(window, show="*", textvariable=passwordVar)

loginBtn = Button(window, text="Login", command=checkLogin)

lbl1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)

lbl2.grid(row = 1, column = 0)
entry2.grid(row = 1, column = 1)

# sticky - naaldah tseguudiig zaaj ugno, w/e/s/n -iin ali 1 esvel kombinats baij bolno
loginBtn.grid(row = 2, column = 0, columnspan = 2, sticky = "we")

window.mainloop()