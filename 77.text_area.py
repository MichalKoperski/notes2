from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)



window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Arial",25),
            height=4,
            width=10,
            padx=20,
            pady=20,
            fg='red')

text.pack()
button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()