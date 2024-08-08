from tkinter import *

def doSomething(event):
    print("Mouse coordinates: "+str(event.x)+" , "+str(event.y))


window = Tk()

window.bind("<Button-1>",doSomething)   #lewy przycisk
window.bind("<Button-2>",doSomething)   #scroll
window.bind("<Button-3>",doSomething)   #prawy przycisk
window.bind("<ButtonRelease>",doSomething)
window.bind("<Enter>",doSomething)      #enter the window with mouse
window.bind("<Leave>",doSomething)      #leave the window with mouse
window.bind("<Motion>",doSomething)      #move of mouse

window.mainloop()