import mysql.connector as mql

def convert_to_bd(filename):
    with open(filename, "rb") as file:
        bd = file.read()
    return bd
file = convert_to_bd(r"C:\Users\User\OneDrive\Documents\GitHub\mySQL\hi.jpg")
mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
            )
print("Data connected successfuly.")
cursor = mydb.cursor()
sql = "insert into employees image values %s"
val = (file,)
cursor.execute(sql, val)
mydb.commit() 
mydb.close()

