from tkinter import *
from tkinter import ttk
root = Tk()


Label(root, text="Name:").grid(row=0, column=0, sticky="e")
Label(root, text="Email:").grid(row=1, column=0, sticky="e")
Label(root, text="Password:").grid(row=2, column=0, sticky="e")


root.mainloop()

