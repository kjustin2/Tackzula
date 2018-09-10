import os
import tkinter as tk
from tkinter import messagebox
from character import Character

# Create root frame and initialize saving ability
root = tk.Tk()
can_save = True


# Create initial frame
def initial_frame():
    back = tk.Frame(master=root, bg='black')
    back.pack_propagate(0)
    back.pack(fill=tk.BOTH, expand=1)
    return back


# Saving options
def save_options():
    main_frame.pack_forget()
    save_frame = initial_frame()


# Save button
def ask_save():
    if can_save:
        if tk.messagebox.askyesno('Save', 'Do you want to save?') and can_save:
            save_options()
        else:
            root.destroy()
    else:
        root.destroy()


# Play button
def play_button():
    if tk.messagebox.askyesno('Verify', 'Really quit?'):
        root.destroy()
    else:
        tk.messagebox.showinfo('No', 'Quit has been cancelled')


# Load button
def load_button():
    load.pack_forget()


# Start of game

# Create main screen
root.title("Tackzula")
root.geometry("1280x800")
root.resizable(0, 0)
root.iconbitmap("sword.ico")

# Create Initial Screen
main_frame = initial_frame()
main_title = tk.Label(main_frame, bg="black", text="Tackzula", fg="blue", font=("Times", 70))
main_title.pack(pady=50)

play = tk.Button(master=main_frame, bg="black", text='Play', fg="blue", font=("Times", 70), width=25, command=play_button)
play.pack(pady=50)

load = tk.Button(master=main_frame, bg="black", text='Load Game', fg="blue", font=("Times", 70), width=25, command=load_button)
load.pack(pady=50)
# End Initial Screen

# Main loop runner
root.protocol("WM_DELETE_WINDOW", ask_save)
root.mainloop()

