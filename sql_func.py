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

    # print(flag)
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



def input_teacher_details(id,name,age,gender,email,contact):
    query = "INSERT INTO teacher VALUES (%s,%s,%s,%s,%s,%s);"
    val = (str(id),str(name),str(age),str(email),str(contact),str(gender))
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