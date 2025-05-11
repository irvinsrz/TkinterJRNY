from tkinter import *

def display():
    if (x.get()==1 and y.get()==0):
        print("I like Python")
    elif (x.get()==0 and y.get()==1):
        print("I like Java")
    elif (x.get()==1 and y.get()==1):  
        print("I like both Python and Java")
    else:
        print("I don't like either")
        

window = Tk()

x = IntVar()
y = IntVar()

checkbox = Checkbutton(window,text='Python',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.config(font=('arial',15))
checkbox.config(fg='purple',bg='black')
checkbox.config(activeforeground="purple")
checkbox.config(activebackground='black')
checkbox.pack()
photo = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\IrvGrind.py\\PYTHONTKINTER\\python2.png')
checkbox.config(image=photo,compound=RIGHT)

checkbox2 = Checkbutton(window,text='Java',variable=y,onvalue=1,offvalue=0,command=display)
checkbox2.config(font=('arial',15))
checkbox2.config(fg='purple',bg='black')
checkbox2.config(activeforeground="purple")
checkbox2.config(activebackground='black')
checkbox2.pack()
photo2 = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\IrvGrind.py\\PYTHONTKINTER\\java.png')
checkbox2.config(image=photo,compound=RIGHT)


window.mainloop()