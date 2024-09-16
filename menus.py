import tkinter as tk

root = tk.Tk()
root.title("Menu")
root.geometry("500x400")

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff='OFF')
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
menu.add_cascade(label='File', menu=file_menu)

result_menu = tk.Menu(menu, tearoff='OFF')
result_menu.add_checkbutton(label='Picture')
result_menu.add_checkbutton(label='Music')
menu.add_cascade(label='Option', menu=result_menu)

root.configure(menu=menu)

root.mainloop()
