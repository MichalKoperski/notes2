from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

window = Tk()

fileImage = PhotoImage(file="logo.png")

menubar = Menu(window)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=fileImage,compound="left")
#fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,compound='left')
window.config(menu=menubar)
window.mainloop()