#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from db import DBConnect
from listComp import ListComp

#Config
conn = DBConnect()
root = Tk()
root.geometry('1920x1080')
root.title('Feedback Resolution Hub')
root.configure(background='#292421')

def on_comment_click(event):
    if comment.get("1.0", "end-1c") == "Enter your comment here":
        comment.delete("1.0", tk.END)
        comment.config(fg='black')  # Change text color to black

def on_comment_leave(event):
    if comment.get("1.0", "end-1c") == "":
        comment.insert("1.0", "Enter your comment here")
        comment.config(fg='grey')  # Change text color to grey

def on_entry_click(event):
    if entry.get() == "Full Name":
        entry.delete(0, tk.END)
        entry.config(fg='gray')  # Change text color to black

def on_entry_leave(event):
    if entry.get() == "":
        entry.insert(0, "Full Name")
        entry.config(fg='gray')  # Change text color to grey



root.title("My UI")  # Set the title of the window

# Heading label
heading_label = ttk.Label(root, text="Feedback Resolution Hub", font=('Agency FB', 32, 'bold'), background='#000000', foreground='white')
heading_label.pack(pady=20)

# Load the background image
background_image = tk.PhotoImage(file="D:\Complaint-Management-System-Project-IN-Python-master\png-transparent-simple-white-honeycomb-pattern-background-white-polygon-honeycomb-thumbnail.png")  # Replace with your image file path

# Create a Canvas for the background image
canvas = tk.Canvas(root, width=background_image.width(), height=background_image.height())
canvas.pack()

# Place the background image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)


# Place the button at the center
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))  # Adjust the font size as needed

BuSubmit = Button(root, text="Submit Now",style='TButton', padding=(30, 20))
BuSubmit.pack(pady=20, padx=20)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_center = (screen_width - BuSubmit.winfo_reqwidth()) // 2
y_center = (screen_height - BuSubmit.winfo_reqheight()) // 2
BuSubmit.place(x=700, y=640)



#Entries

entry = tk.Entry(root,width=50, font=('Arial', 16))
entry.insert(0, "Full Name")  # Initial hint text
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_entry_leave)
entry.place(x=420, y=150)

#Button
style.configure('TRadiobutton', background='#DCDCDC')
style = ttk.Style()
style.configure('TRadiobutton', font=('Helvetica', 16))  # Adjust the font size as needed
SpanGender = StringVar()
Radiobutton(root, text='Male', value='male', variable=SpanGender,style='TRadiobutton',padding=(20, 10)).place(x=600, y=200)
Radiobutton(root, text='Female', value='female', variable=SpanGender,style='TRadiobutton',padding=(20, 10)).place(x=800, y=200)

#comment box
comment = tk.Text(root, height=12, width=100, wrap=tk.WORD,font=('Arial', 16))
comment.insert("1.0", "Enter your comment here")  # Initial hint text
comment.config(fg='grey')  # Set initial text color to grey
comment.bind("<FocusIn>", on_comment_click)
comment.bind("<FocusOut>", on_comment_leave)
comment.place(x=160, y=300)

#brought to you by code-projects.org
def SaveData():
	msg = conn.Add(entry.get(), SpanGender.get(), comment.get(1.0, 'end'))
	entry.delete(0, 'end')
	comment.delete(1.0, 'end')
	showinfo(title='Add Info', message=msg)

def ShowList():
	listrequest = ListComp()


BuSubmit.config(command=SaveData)


root.mainloop()
