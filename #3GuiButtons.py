#button = you click it, then it does stuff

from tkinter import *
from PIL import Image, ImageTk

count = 0

def click():
    global count
    count = count + 1
    label.config(text=count)


window = Tk()

button = Button(window,text="Click me!")
button.config(command=click)
button.config(font=('arial',30,'bold'))
button.config(bg='purple')
button.config(fg='red')
button.config(activebackground='green')
button.config(activeforeground='blue')
#image = PhotoImage(file='fblogo.png')
#button.config(image=image)
#button.config(compound='bottom')
label = Label(window,text=count)
label.config(font=('Monospace'))
label.pack()
button.pack()


window.mainloop()