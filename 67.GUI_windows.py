# widgets   =   GUI elements: buttons, textboxes, labels, images
# windows   =   serves as a container to hold or contain these widgets

from tkinter import *

window = Tk()   #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#5cfcff")

window.mainloop()   #place window on computer screen, listen for events