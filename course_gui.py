import tkinter as tk
import main_screen_gui as msg
import validity_checker as vc
import sql_func as sf

def get_add_course_details(e1,e2,frame_bottom):
    course_id = e1.get()
    course_name = e2.get()
    flag = vc.get_add_course_details_check(course_id,course_name)
    if(flag==True):
        query = sf.input_course_details(course_id,course_name)
        if(query==True):
            label_frame_bottom = tk.Label(master=frame_bottom,text="Done",font=("Roboto",15),bg="white")
            label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
        else:
            label_frame_bottom = tk.Label(master=frame_bottom,text="Inalid Input Query",font=("Roboto",15),bg="white")
            label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    else:
        label_frame_bottom = tk.Label(master=frame_bottom,text="Inalid Input",font=("Roboto",15),bg="white")
        label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label_frame_bottom.after(1000,label_frame_bottom.destroy)


def add_course_details(window,frame2,frame3):
    print("add course details")
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

    label1_frame_left = tk.Label(master=frame_left,text="Course Id",font=("Roboto",15),bg="white")
    label2_frame_left = tk.Label(master=frame_left,text="Name",font=("Roboto",15),bg="white")

    entry1_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry2_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))

    button_frame_bottom = tk.Button(master=frame_bottom,text="Add",font=("Roboto",10),relief=tk.GROOVE,command=lambda:get_add_course_details(entry1_frame_right,entry2_frame_right,frame_bottom))
    button_frame_bottom.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label2_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    entry1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry2_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)


    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)


    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:course_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)


def get_teacher_course_set(e1,e2,frame_bottom):
    teacher_id = e1.get()
    course_id = e2.get()


    query = sf.teacher_course_set(teacher_id,course_id)
    if(query==True):
        label_frame_bottom = tk.Label(master=frame_bottom,text="Done",font=("Roboto",15),bg="white")
        label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)
    else:
        label_frame_bottom = tk.Label(master=frame_bottom,text="Inalid Input Query",font=("Roboto",15),bg="white")
        label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label_frame_bottom.after(1000,label_frame_bottom.destroy)

def teacher_course_set(window,frame2,frame3):
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

    label1_frame_left = tk.Label(master=frame_left,text="Course Id(Req)",font=("Roboto",15),bg="white")
    label2_frame_left = tk.Label(master=frame_left,text="Teacher Id(Req)",font=("Roboto",15),bg="white")

    entry1_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry2_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))

    button_frame_bottom = tk.Button(master=frame_bottom,text="Update",font=("Roboto",10),relief=tk.GROOVE,command=lambda:get_teacher_course_set(entry1_frame_right,entry2_frame_right,frame_bottom))
    button_frame_bottom.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label2_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    entry1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry2_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)


    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)


    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:course_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)



def get_student_course_set(e1,e2,frame_bottom):
    student_id = e1.get()
    course_id = e2.get()
    
    query = sf.student_course_set(student_id,course_id)
    if(query==True):
        label_frame_bottom = tk.Label(master=frame_bottom,text="Done",font=("Roboto",15),bg="white")
        label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)
    else:
        label_frame_bottom = tk.Label(master=frame_bottom,text="Inalid Input Query",font=("Roboto",15),bg="white")
        label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label_frame_bottom.after(1000,label_frame_bottom.destroy)

def student_course_set(window,frame2,frame3):
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

    label1_frame_left = tk.Label(master=frame_left,text="Course Id(Req)",font=("Roboto",15),bg="white")
    label2_frame_left = tk.Label(master=frame_left,text="Student Id(Req)",font=("Roboto",15),bg="white")

    entry1_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))
    entry2_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))

    button_frame_bottom = tk.Button(master=frame_bottom,text="Update",font=("Roboto",10),relief=tk.GROOVE,command=lambda:get_student_course_set(entry1_frame_right,entry2_frame_right,frame_bottom))
    button_frame_bottom.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label2_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    entry1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)
    entry2_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)


    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)


    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:course_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)



def get_delete_course_details(e1,frame_bottom):
    course_id = e1.get()
    id_is_valid = sf.is_valid_course_id(course_id)
    if(id_is_valid):
        sf.delete_course(course_id)
        e1.delete(0,tk.END)
        label_frame_bottom = tk.Label(master=frame_bottom,text="Done",font=("Roboto",15),bg="white")
        label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)
    else:
        label_frame_bottom = tk.Label(master=frame_bottom,text="Inalid Input",font=("Roboto",15),bg="white")
        label_frame_bottom.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)
    label_frame_bottom.after(1000,label_frame_bottom.destroy)


def delete_course_details(window,frame2,frame3):
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

    label1_frame_left = tk.Label(master=frame_left,text="Course Id(Req)",font=("Roboto",15),bg="white")

    entry1_frame_right = tk.Entry(master=frame_right,font=("Roboto",15))

    button_frame_bottom = tk.Button(master=frame_bottom,text="Delete",font=("Roboto",10),relief=tk.GROOVE,command=lambda:get_delete_course_details(entry1_frame_right,frame_bottom))
    button_frame_bottom.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)

    label1_frame_left.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=10,pady=10)

    entry1_frame_right.pack(side=tk.TOP,fill=tk.X,expand=True,padx=10,pady=10)


    frame_left.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    frame_right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)


    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:course_details(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)



def course_details(window,frame2,frame3):
    frame2.destroy()
    frame2=tk.Frame(master=window,bg="#e6e6ff")
    frame2.pack(fill=tk.BOTH,expand=True)

    button2_frame2 = tk.Button(master=frame2,text="Add\nCourse\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: add_course_details(window,frame2,frame3))
    button1_frame2 = tk.Button(master=frame2,text="Teacher-\nCourse",font=("Roboto",20),relief=tk.GROOVE,command=lambda: teacher_course_set(window,frame2,frame3))
    button3_frame2 = tk.Button(master=frame2,text="Student-\nCourse",font=("Roboto",20),relief=tk.GROOVE,command=lambda: student_course_set(window,frame2,frame3))
    button4_frame2 = tk.Button(master=frame2,text="Delete\nCourse\nDetails",font=("Roboto",20),relief=tk.GROOVE,command=lambda: delete_course_details(window,frame2,frame3))
    button2_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button1_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button3_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)
    button4_frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,padx=15,pady=80)

    frame3.destroy()
    frame3=tk.Frame(master=window,bg="#e6e6ff")
    frame3.pack(fill=tk.X,side=tk.BOTTOM)

    button2_frame3 = tk.Button(master=frame3,text="Back",padx=40,pady=3,font=("Roboto",10),command=lambda:msg.home_screen(window,frame2,frame3),relief=tk.GROOVE)
    button1_frame3 = tk.Button(master=frame3,text="Exit",padx=40,pady=3,font=("Roboto",10),command=window.destroy,relief=tk.GROOVE)
    button1_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
    button2_frame3.pack(side=tk.RIGHT,padx=5,pady=5)
