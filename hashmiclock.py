from tkinter import *
from tkinter.ttk import *
from tkinter import Label
Tk import time

from time import strftime

root= Tk()
root.title("Clock")


label.pack(anchor='center')

def time():
	string=strftime('%H:%M:%S %p')
	label.config(text=string)
	label.after(1000, time)

label = Label(root, font=("DS-DIGI", 80), background = "black", foreground="cyan")
label.pack(anchor='center')
time()


mainloop()	

