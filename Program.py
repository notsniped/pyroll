# Imports
import atexit
from tkinter import *
from tkinter import messagebox
import webbrowser

# Variables
root = Tk()

# Window Configuration
root.title("amogus")
root.geometry("350x350")
root.resizable(False, False)
root.config(background="#121212")

# Pre-defined methods
def exit_handler():
    messagebox.showinfo("Imagine being oversmart", "Trying to escape? lol sussy baka")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Object Mapping
button1 = Button(
    root,
    text="Click me",
    foreground="white",
    background="#151515",
    borderwidth=0.1,
    highlightbackground="#272727",
    highlightcolor="white",
    activebackground="#272727",
    width=30,
    height=20,
    font=(4),
    command=newBrowserWindow
)
button1.pack(pady=125)

atexit.register(exit_handler)
root.mainloop()
