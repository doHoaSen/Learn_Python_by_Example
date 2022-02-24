from distutils import command
from tkinter import *
from turtle import width


#functions
def show_table():
    num = numbox.get()
    num = int(num)
    for i in range(1, 13):
        ans = i * num
        numlist.insert(END, (i, "x", num, "=", ans))
    numbox.delete(0, END)
    numbox.focus()


def clear_list():
    numbox.delete(0, END)
    numlist.delete(0, END)
    numbox.focus()




#main
window = Tk()
window.title("Times Table")
window.geometry("400x300")

#Elements
lb1 = Label(text = "Enter a number: ")
lb1.place(x=20, y=20, width = 100, height=25)

numbox = Entry(text=0)
numbox.place(x=120, y=20, width=100, height=25)
numbox.focus()

numlist = Listbox()
numlist.place(x=120, y=50, width=100, height=220)

#Buttons
btn1 = Button(text = "View Times Table", command= show_table)
btn1.place(x=250, y=20, width=120, height=25)

btn2 = Button(text = "Clear", command= clear_list)
btn2.place(x=250, y=50, width=120, height=25)

window.mainloop()