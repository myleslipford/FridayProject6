from tkinter import *
import tkinter as ttk
root = Tk()

root.geometry("350x200")
# Labels
usernaame= ttk.Label(root, text="Username:")
usernaame.place(x=50, y=30)
password = ttk.Label(root, text="Password:")
password.place(x=50, y=60)


# Entry widgets
username_entry = ttk.Entry(root)
username_entry.place(x=150, y=30)
password_entry = ttk.Entry(root) 
password_entry.place(x=150, y=60)

# Login button
login_button = ttk.Button(root, text="Login")
login_button.place(x=150, y=90)

root.mainloop()