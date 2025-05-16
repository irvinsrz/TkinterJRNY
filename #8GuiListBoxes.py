#listbox =  a listing of selectable text items within it's own container
from tkinter import*

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    for index in food:
        print(str(index))

    #print(listbox.get(listbox.curselection()))
    
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in listbox.curselection():
        listbox.delete(index)
   #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='black',
                  fg='purple',
                  font=('constantia',35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="Submit",font=('constantia',20),command=submit)
submitButton.pack()

addButton = Button(window,text="Add",font=('constantia',20),command=add)
addButton.pack()

deleteButton = Button(window,text="Delete",font=('constantia',20),command=delete)
deleteButton.pack()














window.mainloop()