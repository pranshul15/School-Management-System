# import tkinter as tk


# def on_change(e):
#     print (e.get())
#     e.delete(0, tk.END)

# root = tk.Tk()

# e = tk.Entry(root)
# e.pack()    
# # Calling on_change when you press the return key
# # e.bind("<Return>", lambda:on_change(e))  
# b = tk.Button(root,text="Click",command=lambda:on_change(e))
# b.pack()

# root.mainloop()

import sql_func as sq

data = sq.get_student_details()
k=0
f = k+10 if (k+10)<len(data) else len(data)

for i in range(0,7):
    for j in range(0,f):
        print(data[j][i])