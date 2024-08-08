from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+" degrees C")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,          #orientation of scale
              font=("Arial",20),
              tickinterval=10,          #adds numeric indicators for value
              showvalue=1,              #show/hide current value
              resolution=5,             #increment of slider
              troughcolor='#69EAFF',
              fg='white',
              bg='black')

scale.set((scale['from']-scale['to'])/2)
scale.pack()

button = Button(window,
                text='submit',
                command=submit)
button.pack()
window.mainloop()