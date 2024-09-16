import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x400")

hello = ttk.Label(root, text='Hello', background='red')
welcome = tk.Label(root, text='welcome', background='blue')

# hello.pack(side='left')
# welcome.pack()

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)
# hello.grid(row=1, column=1, sticky='nsew')
# welcome.grid(row=0, column=2, sticky='nsew')

hello.place(x=100, y=100, width=100, height=100)

welcome.place(relx=0.5, rely=0.5)  # this is spred between from 0 to 1
root.mainloop()
