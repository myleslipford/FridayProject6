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


button_row2 = Frame(button_frame1)
button_row2.pack(side=TOP)

button4 = ttk.Button(button_row2, text="4")
button4.pack(side=LEFT)
button5 = ttk.Button(button_row2, text="5")
button5.pack(side=LEFT)
button6 = ttk.Button(button_row2, text="6")
button6.pack(side=LEFT)
button_minus = ttk.Button(button_row2, text="-")
button_minus.pack(side=LEFT)


button_row3 = Frame(button_frame1)
button_row3.pack(side=TOP)

button1 = ttk.Button(button_row3, text="1")
button1.pack(side=LEFT)
button2 = ttk.Button(button_row3, text="2")
button2.pack(side=LEFT)
button3 = ttk.Button(button_row3, text="3")
button3.pack(side=LEFT)
button_multiply = ttk.Button(button_row3, text="*")
button_multiply.pack(side=LEFT)


button_row4 = Frame(button_frame1)
button_row4.pack(side=TOP)

button_clear = ttk.Button(button_row4, text="C")
button_clear.pack(side=LEFT)
button0 = ttk.Button(button_row4, text="0")
button0.pack(side=LEFT)
button_equal = ttk.Button(button_row4, text="=")
button_equal.pack(side=LEFT)
button_divide = ttk.Button(button_row4, text="/")
button_divide.pack(side=LEFT)


root.mainloop()