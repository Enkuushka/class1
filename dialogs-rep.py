from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import codecs

myFileTypes = [
    ("Text",".txt"),
    ("All type", "*")
]

currentFile = ""

def selectFile():
    global currentFile
    filepath = filedialog.askopenfilename(filetypes=myFileTypes)
    # messagebox.showinfo("Selected file name",filepath)
    if(filepath != ""):
        fileHandler = codecs.open(filepath, "r", encoding="utf-8")
        content = ""
        lines = fileHandler.readlines()
        currentFile = filepath
        print("SET Current file: " + currentFile)
        for line in lines:
            content = content + line
        textEntry.insert("2.end", content)
        fileHandler.close()

def saveFile():
    global currentFile
    print("Current file: " + currentFile)
    content = textEntry.get("1.0", "end")
    if(currentFile != ""):
        fileHandler = codecs.open(currentFile, "w", encoding="utf-8")
        fileHandler.writelines(content)
        fileHandler.close()
        messagebox.showinfo("Saved!", "Saved!")
    else:
        filepath = filedialog.asksaveasfilename(filetypes=myFileTypes)
        if(filepath != ""):
            filepath = filepath + ".txt"
            fileHandler = codecs.open(filepath, "w", encoding="utf-8")
            fileHandler.writelines(content)
            fileHandler.close()

def selectFolder():
    filepath = filedialog.askdirectory()
    messagebox.showinfo("Selected folder name", filepath)

def closeFile():
    global currentFile
    currentFile = ""
    textEntry.delete("1.0", "end")

myConfig = [
    {
        "buttonName" : "Open file",
        "function" : selectFile
    },
    {
        "buttonName" : "Save file",
        "function" : saveFile
    },
    {
        "buttonName" : "Select folder",
        "function" : selectFolder
    },
    {
        "buttonName" : "Close file",
        "function" : closeFile
    }
]

window = Tk()
frame1 = Frame(window)
for btnConfig in myConfig:
    btn = Button(frame1, text = btnConfig["buttonName"]\
        , command = btnConfig["function"])
    btn.pack(side = LEFT)

textEntry = Text(window, height = 10, width = 80)
frame1.grid(row = 0, column = 0)
textEntry.grid(row = 1, column = 0)

window.mainloop()