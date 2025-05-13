#radio button = similar to checkbox, but you can only select one from a group
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

food = ["pizza","humburger","hotdog"]
def order():
    if(x).get()==0:
        print("You ordered pizza")
    elif (x).get()==1:
        print("You ordered humburger")
    elif (x).get==2:
        print("You ordered hotdog")
    else:
        print("huh")


window = Tk()


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to a radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index,  # assigns each radiobutton a different value
                              padx= 25, #adds padding on x -axis
                              font=("impact",50),
                              command=order)
    
    radiobutton.pack(anchor=W   )



window.mainloop()