from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import codecs

myFileTypes = [
    ("Text",".txt"),
    ("All type", "*")
]



openFileTabs = []



currentFile = ""
currentFileName = ""

def selectFile():
    global currentFile, currentFileName, window
    filepath = filedialog.askopenfilename(filetypes=myFileTypes)
    # messagebox.showinfo("Selected file name",filepath)
    if(filepath != ""):
        fileHandler = codecs.open(filepath, "r", encoding="utf-8")
        contents = ""
        lines = fileHandler.readlines()
        currentFile = filepath
        currentFileName = filepath
        window.title(currentFileName)
        print("SET Current file: " + currentFile)
        for line in lines:
            contents = contents + line
        fileHandler.close()
        openFileTabs.append(addTab(currentFileName, contents))

def saveFile():
    global notebook, currentFile
    tabid = notebook.select()
    selectedInfo = ""
    for info in openFileTabs:
        if(info["tabid"] == tabid):
            selectedInfo = info
            break

    if(selectedInfo != ""):
        print("Current file: " + currentFile)
        currentFile = selectedInfo["filepath"]
        textEntry = selectedInfo["textEntry"]
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
    else:
        messagebox.showerror("Error", "Програмын openFileTabs дотор Таб олдсонгүй!")

def selectFolder():
    filepath = filedialog.askdirectory()
    messagebox.showinfo("Selected folder name", filepath)

def closeFile():
    global currentFile
    currentFile = ""
    currentFileName = ""
    window.title("Tk")
    textEntry.delete("1.0", "end")

def addTab(name, contents):
    global notebook, window
    frame = Frame(window)
    textEntry = Text(frame, height = 10, width = 80)
    textEntry.insert("1.0", contents)
    textEntry.pack()
    notebook.add(frame, text=name)
    tabsss = notebook.tabs()
    lastTabId = tabsss[-1]
    notebook.select(lastTabId)
    return {
        "filepath" : name,
        "tabid" : lastTabId,
        "textEntry" : textEntry
    }

def getSelectedTab():
    global notebook
    print(notebook.select())
    # for tabid in notebook.tabs():
    #     print(notebook.tab(tabid))

window = Tk()

menubar = Menu(window)
fileMenu = Menu(menubar)
menubar.add_cascade(label = "File", menu=fileMenu)

fileMenu.add_command(label = "Open file", command = selectFile)
fileMenu.add_command(label = "Save file", command = saveFile)
fileMenu.add_command(label = "Select folder", command = selectFolder)
fileMenu.add_command(label = "Close file", command = closeFile)

fileMenu.add_command(label = "Test", command = getSelectedTab)

window["menu"] = menubar

notebook = ttk.Notebook(window)

notebook.pack()


window.mainloop()