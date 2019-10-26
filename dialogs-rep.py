from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import codecs

myFileTypes = [
    ("Text",".txt"),
    ("All type", "*")
]



# openFiles = [
#     {
#         filePath: "",
#         tabId: ""
#     }
# ]



currentFile = ""
currentFileName = ""

def selectFile():
    global currentFile, currentFileName, window
    filepath = filedialog.askopenfilename(filetypes=myFileTypes)
    # messagebox.showinfo("Selected file name",filepath)
    if(filepath != ""):
        fileHandler = codecs.open(filepath, "r", encoding="utf-8")
        content = ""
        lines = fileHandler.readlines()
        currentFile = filepath
        currentFileName = filepath
        window.title(currentFileName)
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
    currentFileName = ""
    window.title("Tk")
    textEntry.delete("1.0", "end")

def addTab():
    global notebook, window
    frame = Frame(window)
    textEntry = Text(frame, height = 10, width = 80)
    textEntry.pack()
    notebook.add(frame, text='New tab')
    tabsss = notebook.tabs()
    lastTabId = tabsss[-1]
    notebook.select(lastTabId)

window = Tk()

menubar = Menu(window)
fileMenu = Menu(menubar)
menubar.add_cascade(label = "File", menu=fileMenu)

fileMenu.add_command(label = "Open file", command = selectFile)
fileMenu.add_command(label = "Save file", command = saveFile)
fileMenu.add_command(label = "Select folder", command = selectFolder)
fileMenu.add_command(label = "Close file", command = closeFile)

fileMenu.add_command(label = "Test add tab", command = addTab)

window["menu"] = menubar

# textEntry.grid(row = 0, column = 0, sticky = "nwes")

notebook = ttk.Notebook(window)
f1 = Frame(notebook)
f2 = Frame(notebook)
notebook.add(f1, text='Tab 1')
notebook.add(f2, text='Tab 2')

textEntry = Text(f1, height = 10, width = 80)
textEntry.pack()

notebook.pack()

print(notebook.tabs())

notebook.tab(".!notebook.!frame2", state="disabled")
print(notebook.tab(".!notebook.!frame2"))

window.mainloop()