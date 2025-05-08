from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

#entry widget = textbox that accepts a single line of user input
 
def submit():
    username = entry.get() #get the input from the entry widget
    print("Hello,",username) #print the input to the console

def delete():
    entry.delete(0,END) #delete the input from the entry widget
    print("Deleted") #print to the 

def backspace():
    entry.delete(len(entry.get())-1,END) #delete the last character from the entry widget


window = tk.Tk()
window.title("User Input")
window.config(bg='white')



submit = Button(window,text="Submit",command=submit)
submit.pack(side=RIGHT)

delete = Button(window,text="Delete",command=delete)
delete.pack(side=RIGHT)

backspace = Button(window,text="Backspace",command=backspace)
backspace.pack(side=RIGHT)

entry = Entry()
entry.config(font=('Ink Free',50))
entry.config(bg='purple')
entry.config(fg='green')
#entry.insert(0,'Username:')
#entry.config(state='disabled') #disables the entry widget so the user cannot edit it
entry.config(width=10)
#entry.config(show='*') #shows the input as asterisks
entry.pack()


window.mainloop()