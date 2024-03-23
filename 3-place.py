from tkinter import *
import tkinter as ttk
root = Tk()

root.geometry("350x200")
# Labels
usernaame= ttk.Label(root, text="Username:")
usernaame.place(x=50, y=30)
password = ttk.Label(root, text="Password:")
password.place(x=50, y=60)


