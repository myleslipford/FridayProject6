from tkinter import *
from tkinter import ttk
root = Tk()


name = ttk.Label(root, text="Name:")
name.grid(row=0, column=0, sticky="e")

email = ttk.Label(root, text="Email:")
email.grid(row=1, column=0, sticky="e")

password = ttk.Label(root, text="Password:")
password.grid(row=2, column=0, sticky="e")

name_entry = Entry(root)
email_entry = Entry(root)
password_entry = Entry(root)  
name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

sign_up_button = ttk.Button(root, text="Sign Up Now")
sign_up_button.grid(row=3, columnspan=2)

root.mainloop()

