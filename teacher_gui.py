import tkinter as tk
import main_screen_gui as msg

#teacher
def add_teacher_details(window,frame2,frame3):
    print("add teacher details")

    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)    

    frame_left = tk.Frame(master=frame2,bg="white")
    frame_right = tk.Frame(master=frame2,bg="white")
    frame_bottom = tk.Frame(master=frame2,bg="white")
    frame_bottom.pack(side=tk.BOTTOM,fill=tk.X)

    label1_frame_left = tk.Label(master=frame_left,text="Teacher Id",font=("Roboto",15),bg="white")
    label2_frame_left = tk.Label(master=frame_left,text="Name",font=("Roboto",15),bg="white")
    label3_frame_left = tk.Label(master=frame_left,text="Age",font=("Roboto",15),bg="white")
    label4_frame_left = tk.Label(master=frame_left,text="Gender",font=("Roboto",15),bg="white")
    label5_frame_left = tk.Label(master=frame_left,text="Email",font=("Roboto",15),bg="white")
    label6_frame_left = tk.Label(master=frame_left,text="Contact",font=("Roboto",15),bg="white")

    entry1_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry2_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry3_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry4_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry5_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry6_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))

    button_frame_bottom = tk.Button(master=frame_bottom,text="Add",font=("Roboto",10),relief=tk.GROOVE)
    button_frame_bottom.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label2_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label3_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label4_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label5_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label6_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    entry1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry2_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry3_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry4_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry5_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry6_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)


    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)


    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:teacher_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)



def view_teacher_details(window,frame2,frame3):
    print("view teacher details")
    
    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    frame_left = tk.Frame(master=frame2,bg="white")
    frame_middle = tk.Frame(master=frame2,bg="white")
    frame_right = tk.Frame(master=frame2,bg="white")
    frame_bottom = tk.Frame(master=frame2,bg="white")
    frame_bottom.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

    label1_frame_left = tk.Label(master=frame_left,text="Teacher's Id:",font=("Roboto",15),bg="white")
    entry1_frame_middle = tk.Entry(master=frame_middle,font=("Roboto",15))
    button1_frame_right = tk.Button(master=frame_right,text="View",font=("Roboto",10),relief=tk.GROOVE)
    
    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    entry1_frame_middle.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    button1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)

    frame_left.pack(side=tk.LEFT,fill=tk.X,expand=True)
    frame_middle.pack(side=tk.LEFT,fill=tk.X,expand=True)
    frame_right.pack(side=tk.LEFT,fill=tk.X,expand=True)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:teacher_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)


def update_teacher_details(window,frame2,frame3):
    print("update teacher details")

    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    frame_left = tk.Frame(master=frame2,bg="white")
    frame_right = tk.Frame(master=frame2,bg="white")
    frame_bottom = tk.Frame(master=frame2,bg="white")
    frame_bottom.pack(side=tk.BOTTOM,fill=tk.X)

    label1_frame_left = tk.Label(master=frame_left,text="Teacher Id(Req)",font=("Roboto",15),bg="white")
    label2_frame_left = tk.Label(master=frame_left,text="Name",font=("Roboto",15),bg="white")
    label3_frame_left = tk.Label(master=frame_left,text="Age",font=("Roboto",15),bg="white")
    label4_frame_left = tk.Label(master=frame_left,text="Gender",font=("Roboto",15),bg="white")
    label5_frame_left = tk.Label(master=frame_left,text="Email",font=("Roboto",15),bg="white")
    label6_frame_left = tk.Label(master=frame_left,text="Contact",font=("Roboto",15),bg="white")

    entry1_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry2_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry3_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry4_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry5_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry6_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))

    button_frame_bottom = tk.Button(master=frame_bottom,text="Update",font=("Roboto",10),relief=tk.GROOVE)
    button_frame_bottom.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label2_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label3_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label4_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label5_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label6_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    entry1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry2_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry3_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry4_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry5_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry6_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)


    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)


    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:teacher_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)




def delete_teacher_details(window,frame2,frame3):
    print("delete teacher details")

    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:teacher_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)


def teacher_details(window,frame2,frame3):
    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)
    button1_frame2 = tk.Button(master=frame2,text="View\nTeacher\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: view_teacher_details(window,frame2,frame3))
    button2_frame2 = tk.Button(master=frame2,text="Add\nTeacher\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: add_teacher_details(window,frame2,frame3))
    button3_frame2 = tk.Button(master=frame2,text="Update\nTeacher\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: update_teacher_details(window,frame2,frame3))
    button4_frame2 = tk.Button(master=frame2,text="Delete\nTeacher\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: delete_teacher_details(window,frame2,frame3))
    button1_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button2_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button3_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button4_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)

    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:msg.home_screen(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
