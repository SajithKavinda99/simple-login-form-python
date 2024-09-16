import tkinter as tk
from tkinter import ttk

home = tk.Tk()
home.title("My first project")
home.iconbitmap('plus.png')
width, height = 400, 400
home.geometry(f'{400}x{400}')
home.resizable(False, False)
display_width = home.winfo_screenwidth()
display_height = home.winfo_screenheight()
left = int(display_width/2-width/2)
top = int(display_height/2-height/2)
home.geometry(f'{400}x{400}+{left}+{top}')

label_heading = ttk.Label(home, text="WELCOME TO APP", font=25, padding=20)
label_heading.pack()

frame_username = ttk.Frame(home, width=350, height=50, relief=tk.GROOVE)
frame_username.pack_propagate(False)
frame_username.pack()
label_username = ttk.Label(frame_username, text="User Name", font=15)
label_username.pack(side=tk.LEFT, padx=(10, 10), pady=0)
entry_username = ttk.Entry(frame_username, width=100)
entry_username.pack(side=tk.LEFT, padx=(0, 10), pady=10)

frame_password = ttk.Frame(home, width=350, height=50, relief=tk.GROOVE)
frame_password.pack_propagate(False)
frame_password.pack()
lebel_password = ttk.Label(frame_password, text="Password", font=15)
lebel_password.pack(side=tk.LEFT, padx=(10, 10), pady=0)
entry_password = ttk.Entry(frame_password, width=100)
entry_password.pack(side=tk.LEFT, padx=(10, 10), pady=10)

button_login = ttk.Button(home, text="Log in", padding=20, width=50)
button_login.pack(pady=20)

home.mainloop()
