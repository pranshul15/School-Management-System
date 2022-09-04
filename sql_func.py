import mysql.connector


def sql_connection_with_database():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    flag = False

    for x in mycursor:
        if((x[0]) == "dbms_project_database"):
            flag = True
            break

    if(flag == False):
        mucursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE dbms_project_database")

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )

    print("DateBase Connected")

def input_student_details(id,name,age,standard,gender,email,contact):
    query = "INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s);"
    val = (str(id),str(name),str(standard),str(age),str(email),str(contact),str(gender))
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        return False
    return True


def get_student_details():
    query = "SELECT * FROM student;"
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

def is_valid_student_id(student_id):
    query = "SELECT * FROM student WHERE id = %s;"
    val = (str(student_id),)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    if(mycursor.fetchone()):
        return True
    print("error valid")
    return False



def update_student(id,name,attribute):
    query = "UPDATE student SET "+attribute+" = %s WHERE id = %s;"
    val = (str(name),str(id))
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        print("error")



def delete_student(id):
    query = "DELETE FROM student WHERE id = %s;"
    val = (str(id),)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        print("error")





def input_teacher_details(id,name,age,gender,email,contact):
    query = "INSERT INTO teacher VALUES (%s,%s,%s,%s,%s,%s);"
    val = (str(id),str(name),str(age),str(email),str(contact),str(gender))
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    print(query)
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        return False
    return True

def get_teacher_details():
    query = "SELECT * FROM teacher;"
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def is_valid_teacher_id(teacher_id):
    query = "SELECT * FROM teacher WHERE id = %s;"
    val = (str(teacher_id),)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    if(mycursor.fetchone()):
        return True
    print("error valid")
    return False

def update_teacher(id,name,attribute):
    query = "UPDATE teacher SET "+attribute+" = %s WHERE id = %s;"
    val = (str(name),str(id))
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        print("error")


def delete_teacher(id):
    query = "DELETE FROM teacher WHERE id = %s;"
    val = (str(id),)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        print("error")






def input_course_details(id,name):
    query = "INSERT INTO course VALUES (%s,%s);"
    val = (str(id),str(name))
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        return False
    return True

def teacher_course_set(teacher_id,course_id):
    query = "INSERT INTO teacher_course VALUES (%s,%s);" % (teacher_id,course_id)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query)
        mydb.commit()
    except:
        return False
    return True

def student_course_set(student_id,course_id):
    query = "INSERT INTO student_course VALUES (%s,%s);" % (student_id,course_id)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query)
        mydb.commit()
    except:
        return False
    return True

def is_valid_course_id(course_id):
    query = "SELECT * FROM course WHERE id = %s;"
    val = (str(course_id),)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    if(mycursor.fetchone()):
        return True
    return False

def delete_course(course_id):
    query = "DELETE FROM course WHERE id = %s;"
    val = (str(course_id),)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "15pransh15",
        database = "dbms_project_database"
    )
    mycursor=mydb.cursor()
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except:
        print("error")