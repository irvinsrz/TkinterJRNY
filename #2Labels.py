from tkinter import *
from PIL import Image, ImageTk

#label = an area widget that holds text and/ or  an image within a window

window = Tk()
window.geometry('200x200')

#photo = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\IrvGrind\\PYTHON TKINTER\\facebooklogo.png')

label = Label(window,
              text="Hello World",
              font=('Arial',10,'bold'),
              fg='blue',
              background='black',
              relief=RAISED,
              bd=20,
              padx=20,
              pady=20)
              
  
#label.place(x=0,y=0)
label.pack()


window.mainloop()