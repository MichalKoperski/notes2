from tkinter import *

def doSomething(event):
    label.config(text=event.keysym)


window = Tk()

window.bind("<Key>",doSomething)

label = Label(window,font=("Arial",100))
label.pack()

window.mainloop()