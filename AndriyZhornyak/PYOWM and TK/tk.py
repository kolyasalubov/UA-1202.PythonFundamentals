from tkinter import *

root = Tk() 
root.geometry("500x500") #size
root.resizable(width = False,height = False) #make the windiw unresizeble
root.title("Weather") #name of main widget
root.config(background = "Blue") # background
root["background"] = "white"  # background

label = Label(root,text="Enter the city",font = "Arial 20 ") #creating a mark
label.pack() #illustrating the mark

def click():
   print("g")
button_1 = Button(root,text = 'submit',command = click,font = "Arial 20 ",width = 10,height = 3,background = "BLUE",activebackground = 'green',activeforeground = 'white',fg = "black",padx = "20",pady = "20")
button_1.pack()
button_1.place(y = 270, x = 145)


user_enter = Entry(root)
user_enter.insert(0,"Enter")#add line in enter line
user_enter.insert(5,"....")#add another line

user_enter.pack()

root.mainloop() #illustrate window 

