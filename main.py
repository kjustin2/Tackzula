import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def callback():
    if tk.messagebox.askyesno('Verify', 'Really quit?'):
        tk.messagebox.showwarning('Yes', 'Not yet implemented')
    else:
        tk.messagebox.showinfo('No', 'Quit has been cancelled')

w = tk.Label(root, text="Hello world")
w.pack()
x = "hey"
root.title(x)
button = tk.Button(root, text='stop', width=25, command=callback)
button.pack()

root.mainloop()

#f = open("demo.txt", "w")
#f.write("First line")
#f.close()
#os.remove("demo.txt")
