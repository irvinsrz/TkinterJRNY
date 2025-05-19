from tkinter import*
from tkinter import messagebox #import message box library

def click():
    #messagebox.showinfo(title='This is an info message box',message='you are a person')
    #messagebox.showerror(title='ERROR',message='something went wrong')
    #count = 0
    #while(True):
        #messagebox.showwarning(title='Warning',message='You have a VIRUS')
        #count = count + 1
        #if count == 5:
           #break
    
    #if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
        #print("You did a thing")
    #else:
        #print('You canceled a thing')
        
    #if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):
        #print("You retried a thing")
    #else:
        #print('You canceled a thing')        

    #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
        #print("i like cake too")
    #else:
        #print("Who do you not like cake")

    #answer = (messagebox.askquestion(title='ask question',message='Do you like pie? '))
    #if (answer ==  'yes'):
        #print('i like pie too')
    #else:
        #print("Why do you not like pie")

    answer = (messagebox.askyesnocancel(title='Yes no cancel',message='Do you like to code'))
    if (answer == True):
        print("You like to code")
    elif(answer == False):
        print("Then why are you watching coding?")
    else:
        print('You have dodged the question')
window = Tk()

button = Button(window,command=click,text='click me')
button.pack()



window.mainloop()