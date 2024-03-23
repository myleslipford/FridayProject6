from tkinter import *
from tkinter import ttk
root = Tk()

# Entry box for displaying the expression
entry = Entry(root, width=20, borderwidth=5, state="disabled")
entry.pack(side=TOP)

# Frame for buttons
button_frame1 = Frame(root)
button_frame1.pack(side=TOP)

button_row1 = Frame(button_frame1)
button_row1.pack(side=TOP)

button7 = ttk.Button(button_row1, text="7")
button7.pack(side=LEFT)

button8 = ttk.Button(button_row1, text="8")
button8.pack(side=LEFT)

button9 = ttk.Button(button_row1, text="9")
button9.pack(side=LEFT)

button_plus = ttk.Button(button_row1, text="+")
button_plus.pack(side=LEFT)



root.mainloop()