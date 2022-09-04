import tkinter as tk
from tkinter.font import BOLD
import main_screen_gui as msg

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

    window.after(500,msg.main_screen)
    window.after(500,window.destroy)
    window.mainloop()