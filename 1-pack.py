from tkinter import *
from tkinter import ttk
root = Tk()

# Entry box for displaying the expression
entry = Entry(root, width=20, borderwidth=5, state="disabled")
entry.pack(side=TOP)

# Frame for buttons
button_frame = Frame(root)
button_frame.pack(side=TOP)


root.mainloop()