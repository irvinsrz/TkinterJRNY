from tkinter import *
from PIL import Image, ImageTk


def submit():
    print("The temperature is: " + str(scale.get()) + " degree C")


window = Tk()

hot_image = Image.open("C:/Users/Lenovo/Desktop/IrvGrind.py/PYTHONTKINTER/flame.png")
resized_hot = hot_image.resize((50,50))
photo = ImageTk.PhotoImage(resized_hot)
hot = Label(window,image=photo)
hot.pack()



scale = Scale(window,
              from_=100,to=0,
              length=500,
              font=('consolas',20),
              tickinterval=10,
              #showvalue=0 #hide current value
              troughcolor='purple',
              fg='red',
              bg='black')
#scale.set(50)
scale.pack()

snow_image = Image.open("C:/Users/Lenovo/Desktop/IrvGrind.py/PYTHONTKINTER/snowflakes.png")
resized_snow = snow_image.resize((50,50))
snows = ImageTk.PhotoImage(resized_snow)
snow = Label(window,image=snows)
snow.pack(anchor=S)



button = Button(window,text='Submit',command=submit,font=('consolas',12),padx=100)
button.pack()




window.mainloop()