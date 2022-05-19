import mysql.connector

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
    mycursor.execute("CREATE DATABASE dbms_project_database")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "15pransh15",
    database = "dbms_project_database"
)

