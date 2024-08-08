from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered pizza")
    elif(x.get() == 1):
        print("You ordered hamburger")
    elif (x.get() == 2):
        print("You ordered hotdog")
    else:
        print("ha")
window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x,       #groups radiobuttons together if they share the same variable
                              value=index,      #assigns each radiobutton a different value
                              padx=25,
                              font=("Impact",50),
                              indicator=0,      #eliminate circle indicators
                              width=10,         #sets width the radio buttons
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()