import tkinter as tk
from tkinter import messagebox
import main_screen_gui as msg
import validity_checker as vc
import sql_func as sf



def get_add_teacher_details(entries):
    teacher_id = entries[0].get()
    teacher_name = entries[1].get()
    teacher_age = entries[2].get()
    teacher_gender = entries[3].get()
    teacher_email = entries[4].get()
    teacher_contact = entries[5].get()
    flag = vc.get_add_teacher_details_check(teacher_id,teacher_name,teacher_age,teacher_gender,teacher_email,teacher_contact)
    if(flag==True):
        query = sf.input_teacher_details(teacher_id,teacher_name,teacher_age,teacher_gender,teacher_email,teacher_contact)
        if(query==True):
            messagebox.showinfo(message="Teacher Added")
            for entry in entries:
                entry.delete(0,tk.END)
        else:
            messagebox.showerror(message="Invalid Input")
    else:
        messagebox.showerror(message="Invalid Input")



def add_teacher_details(window,frame2,frame3):
    print("add teacher details")

    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)    

    frame_left = tk.Frame(master=frame2,bg="white")
    frame_right = tk.Frame(master=frame2,bg="white")
    frame_bottom = tk.Frame(master=frame2,bg="white")
    frame_bottom.pack(side=tk.BOTTOM,fill=tk.X)

    labels = ("Teacher Id","First Name","Age","Gender","Email","Contact")
    entries = []
    for lbl in labels:
        temp_label = tk.Label(master=frame_left,text=lbl,font=("Roboto",15),bg="white")
        temp_entry = tk.Entry(master=frame_right,font=("Roboto",15))
        temp_label.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
        temp_entry.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
        entries.append(temp_entry)

    button_frame_bottom = tk.Button(master=frame_bottom,text="Add",font=("Roboto",10),relief=tk.GROOVE,command=lambda:get_add_teacher_details(entries))
    button_frame_bottom.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)


    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:teacher_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)



def view_teacher_details(window,frame2,frame3,k=0):
    print("view teacher details")
    
    frame2.destroy()
    frame2=tk.Frame(master=window,bg="White")
    frame2.pack(fill=tk.BOTH,expand=True)

    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    heading = ("ID","Name","Age","Email","Contact","Gender")

    teacher_data = sf.get_teacher_details()

    for i in range(0,6):
        frame_vertical_frame2 = tk.Frame(master=frame2,bg="white")
        label_vertical_frame = tk.Label(master=frame_vertical_frame2,text=heading[i],font=("Roboto",15,"bold"),bg="White")
        label_vertical_frame.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
        f = k+10 if (k+10)<len(teacher_data) else len(teacher_data)
        for j in range(k,f):
            label_vertical_frame_value = tk.Label(master=frame_vertical_frame2,text=teacher_data[j][i],font=("Roboto",12))
            label_vertical_frame_value.pack(side=tk.TOP,fill=tk.X,expand=True)
        frame_vertical_frame2.pack(fill=tk.Y,side=tk.LEFT,expand=True)

    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:teacher_details(window,frame2,frame3),relief=tk.GROOVE)
    if((k+10)<len(teacher_data)):
        button3_frame3 = tk.Button(master=frame3,text="Next",padx=40,pady=3,font=("Roboto",10),relief=tk.GROOVE,command=lambda:view_teacher_details(window,frame2,frame3,k+10))
    else:
        button3_frame3 = tk.Button(master=frame3,text="Next",padx=40,pady=3,font=("Roboto",10),relief=tk.GROOVE,state=tk.DISABLED)
    if((k-10)>=0):
        button4_frame3 = tk.Button(master=frame3,text="Previous",padx=40,pady=3,font=("Roboto",10),relief=tk.GROOVE,command=lambda:view_teacher_details(window,frame2,frame3,k-10))
    else:
        button4_frame3 = tk.Button(master=frame3,text="Previous",padx=40,pady=3,font=("Roboto",10),relief=tk.GROOVE,state=tk.DISABLED)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button3_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button4_frame3.pack(side=tk.RIGHT,padx=5,pady=5)


def get_update_teacher_details(entries):
    teacher_id = entries[0].get()
    teacher_name = entries[1].get()
    teacher_age = entries[2].get()
    teacher_gender = entries[3].get()
    teacher_email = entries[4].get()
    teacher_contact = entries[5].get()
    id_is_valid = sf.is_valid_teacher_id(teacher_id)
    attribute = ("name","age","gender","email","contact")
    if(id_is_valid==True):
        if(len(str(teacher_name))>0):
            sf.update_teacher(teacher_id,teacher_name,attribute[0])
        if(len(str(teacher_age))>0):
            sf.update_teacher(teacher_id,teacher_age,attribute[1])
        if(len(str(teacher_gender))>0):
            sf.update_teacher(teacher_id,teacher_gender,attribute[2])
        if(len(str(teacher_email))>0):
            sf.update_teacher(teacher_id,teacher_email,attribute[3])
        if(len(str(teacher_contact))>0):
            sf.update_teacher(teacher_id,teacher_contact,attribute[4])
        for entry in entries:
            entry.delete(0,tk.END)
        messagebox.showinfo(message="Teacher Details Updated")
    else:
        messagebox.showerror(message="Invalid Input")


def update_teacher_details(window,frame2,frame3):
    print("update teacher details")

    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    frame_left = tk.Frame(master=frame2,bg="white")
    frame_right = tk.Frame(master=frame2,bg="white")
    frame_bottom = tk.Frame(master=frame2,bg="white")
    frame_bottom.pack(side=tk.BOTTOM,fill=tk.X)

    labels = ("Teacher Id(Req)","Name","Age","Gender","Email","Contact")
    entries = []

    for lbl in labels:
        temp_label = tk.Label(master=frame_left,text=lbl,font=("Roboto",20),bg="white")
        temp_entry = tk.Entry(master=frame_right,font=("Roboto",20))
        temp_label.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
        temp_entry.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
        entries.append(temp_entry)

    button_frame_bottom = tk.Button(master=frame_bottom,text="Update",font=("Roboto",10),relief=tk.GROOVE,command=lambda:get_update_teacher_details(entries))
    button_frame_bottom.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)


    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:teacher_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)


def get_delete_teacher_details(e1):
    teacher_id = e1.get()
    id_is_valid = sf.is_valid_teacher_id(teacher_id)
    if(id_is_valid):
        sf.delete_teacher(teacher_id)
        e1.delete(0,tk.END)
        messagebox.showinfo(message="Teacher Deleted")
    else:
        messagebox.showerror(message="Invalid Input")

def delete_teacher_details(window,frame2,frame3):
    print("delete teacher details")

    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    frame_left = tk.Frame(master=frame2,bg="white")
    frame_right = tk.Frame(master=frame2,bg="white")
    frame_bottom = tk.Frame(master=frame2,bg="white")
    frame_bottom.pack(side=tk.BOTTOM,fill=tk.X)

    label1_frame_left = tk.Label(master=frame_left,text="Teacher's Id(Req)",font=("Roboto",15),bg="white")

    entry1_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))

    button_frame_bottom = tk.Button(master=frame_bottom,text="Delete",font=("Roboto",10),relief=tk.GROOVE,command=lambda:get_delete_teacher_details(entry1_frame_right))
    button_frame_bottom.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    entry1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)


    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)


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
