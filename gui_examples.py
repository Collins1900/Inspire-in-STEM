#!/usr/bin/python

########################
#      gui_examples using tkinter
#      Name : Collins Murimi
#      Date : 7/6/2022
#########################

from tkinter import *

window = Tk()
#Window title 
window.title("My Awesome App")
#window background colour
window.configure(bg="blue")
#window size
window.geometry("700x600") #fix the window size
#labels
f_name = Label(window,text = "first_name", font=("Arial Bold",20))
s_name = Label(window,text = "second_name", font=("Arial Bold ",20))
#labels position
f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)

def open_pop_up():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop up window")
    top.configure(bg = 'green')
    msg = Label(top,text="Welcome to pop up",font = ("mistral", 18,bold)).place(x=150)

#buttons
btn = Button(text="Sign up",bg='blue',fg='purple',command=open_pop_up().pack())
#button position
btn.grid(column = 120 , row = 150)
#text box
txt_box = Entry(window , width = 10)
#text position
txt_box.grid(column = 100, row = 120)

txt_box = Entry(window,width=20)
txt_box,grid(column=100, row = 100)
 
window.mainloop()
