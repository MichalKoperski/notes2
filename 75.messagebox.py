from tkinter import *
from tkinter import messagebox

window = Tk()

def click():
    messagebox.showinfo(title='This is an info message box',message='You are a person')

    messagebox.showerror(title='ERROR',message='something went wrong')

    if messagebox.askokcancel(title='ask ok cancel',message='DO you want to do the thing'):
        print('You did it')
    else:
        print('You canceled')

    if messagebox.askretrycancel(title='ask ok cancel',message='DO you want to retry'):
        print('You did it')
    else:
        print('You canceled')

    if messagebox.askyesno(title='ask yes or no',message='Do you like cake'):
        print('I like cake')
    else:
        print('You dont like cake')

    answer = messagebox.askquestion(title='ask question',message='Do you like pie')
    if(answer == 'YES'):
        print('I like pie too')
    else:
        print('I dont like too')

    answer2 = messagebox.askyesnocancel(title='yes no cancel',message='Do you like to code')
    if(answer2 == True):
        print('You like to code')
    elif(answer == False):
        print('You dont like to code')
    else:
        print('You have dodged the question')

    while(True):
        messagebox.showwarning(title='WARNING!',message='You have a virus')

button = Button(window,
                command=click,
                text='click me')
button.pack()

window.mainloop()