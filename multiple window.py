import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x600")


value = tk.IntVar(value=0)


def increment_value():
    value.set(value.get() + 1)


def create_sub_window():
    sub_window = tk.Toplevel()
    sub_window.geometry("500x600")

    sub_button = ttk.Button(sub_window, text='click me',
                            command=increment_value)
    sub_button.pack()
    sub_label = ttk.Label(sub_window, textvariable=value)
    sub_label.pack()


main_button = ttk.Button(root, text='Open sub window',
                         command=create_sub_window)
main_button.pack()

root.mainloop()
