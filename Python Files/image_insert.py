import mysql.connector as mql

def convert_to_bd(filename):
    with open(filename, "rb") as file:
        bd = file.read()
    return bd
#file = convert_to_bd(r"C:\Users\User\OneDrive\Documents\GitHub\employee-db\Python Files\hi2.png")
file = convert_to_bd("C:/Users/User/Downloads/jefferson.jpg")
mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
            )
print("Data connected successfuly.")
cursor = mydb.cursor()
sql = "update employees set emp_name = %s, emp_phone = %s, emp_sal = %s, image = %s where id = %s"
val = ("Raj", "1234", "49857", file, 3 )
cursor.execute(sql, val)
mydb.commit() 
mydb.close()

