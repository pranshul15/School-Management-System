# # from tkinter import *
# # from tkinter import ttk

# # def load_screen():
# #     root = Tk()
# #     frm = ttk.Frame(root, padding=10)
# #     frm.grid()
# #     ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# #     ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# #     root.mainloop() 
# #Importing the tkinter library
# from tkinter import *

# #Create an instance of tkinter frame
# splash_win= Tk()

# #Set the title of the window
# splash_win.title("Splash Screen Example")

# #Define the size of the window or frame
# splash_win.geometry("700x200")

# #Define the label of the window
# splash_label= Label(splash_win, text= "School Management System", fg= "green",
# font= ('Times New Roman', 40)).pack(pady=20)
# def mainWin():
#    splash_win.destroy()
#    win= Tk()
#    win.title("Main Window")
#    win.geometry("700x200")
#    win_label= Label(win, text= "Main Window", font= ('Helvetica', 25), fg= "red").pack(pady=20)

# #Splash Window Timer

# splash_win.after(3000, mainWin)

# mainloop()
import tkinter as tk
import student_gui as sg
import teacher_gui as tg
import course_gui as cg


def home_screen(window,frame2,frame3):
    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    button1_frame2 = tk.Button(master=frame2,text="Student\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: sg.student_details(window,frame2,frame3))
    button2_frame2 = tk.Button(master=frame2,text="Teacher\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: tg.teacher_details(window,frame2,frame3))
    button3_frame2 = tk.Button(master=frame2,text="Course\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: cg.course_details(window,frame2,frame3))
    button1_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button2_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button3_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)


    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE,state="disabled")
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)


def main_screen():
    window = tk.Tk()
    app_height = 600
    app_width = 800
    window.geometry(f'{app_width}x{app_height}+{350}+{110}')

    frame1 = tk.Frame(master=window,bg="black",padx=5,pady=5)
    label1 = tk.Label(master=frame1,text="SCHOOL MANAGEMENT SYSTEM",font=("Roboto",30),background="black",foreground="White")
    label1.pack()
    frame1.pack(fill=tk.X,expand=False,side=tk.TOP)

    frame2 = tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    frame3 = tk.Frame(master=window,background="#e6e6ff",height=50)
    frame3.pack(fill=tk.X,side=tk.BOTTOM)


    button1_frame2 = tk.Button(master=frame2,text="Student\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: sg.student_details(window,frame2,frame3))
    button2_frame2 = tk.Button(master=frame2,text="Teacher\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: tg.teacher_details(window,frame2,frame3))
    button3_frame2 = tk.Button(master=frame2,text="Course\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: cg.course_details(window,frame2,frame3))
    button1_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button2_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button3_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE,state="disabled")
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)

    # window.after(5000,window.destroy)

    window.mainloop()
