from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import os
from tkinter import filedialog
root = Tk()
root.title("Speakup Menu")
root.iconbitmap("mic.ico")
root.configure(bg="white")

# commands 

def open_speakup():
	os.system('python speakup.py')






image1 = ImageTk.PhotoImage(Image.open("mic.ico"))

prog_label = Label(
	root,
	text="")
prog_label.grid(
	row=2,
	column=3
	)
lab3 = Label(
	root,
	text="",
	fg="black",
	bg="white",
	font=("Arial", 10)
	)
lab3.grid(
	row=2,
	column=2)
lab1 = Label(
	root, 
	image=image1
	)
lab1.grid(
	row=0,
	column=1
	)
lab2 = Label(
	root,
	text="Welcome to Speakup",
	fg="black",
	bg="white",
	font=("Arial", 30)
	)
lab2.grid(
	row=0,
	column=2)
button1 = Button(
	root,
	text="Open Speakup",
	fg="black",
	bg="white",
	font=("Arial", 20),
	command=open_speakup
	)
button1.grid(
	row=1,
	column=2)


root.mainloop()