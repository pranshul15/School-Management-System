# print('''\n\n\t****************************
# \t| School Management System |

# \t****************************



# \t 1. Add Student Data
# \t 2. Add Teacher Data
# \t 3. Add Course Data
# ''')

import tkinter as tk
from tkinter import ttk
import time
from tkinter.font import BOLD
import loader

def wel_src():
    window = tk.Tk()
    window.overrideredirect(True)

    app_height = 600
    app_width = 800
    window.geometry(f'{app_width}x{app_height}+{350}+{130}')

    frame1 = tk.Frame(master=window,bg="yellow")
    label1 = tk.Label(master=frame1,text="SCHOOL\nMANAGEMENT\nSYSTEM",font=("Roboto",40),height=10,width=30)
    label1.pack()
    frame1.pack(fill=tk.BOTH,expand=True)

    window.after(3000,loader.main_screen)
    window.after(3000,window.destroy)
    window.mainloop()