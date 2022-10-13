import tkinter as tk
import io
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("400x250")
import mysql.connector as mql
def photoview():
    mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        )
    cursor = mydb.cursor()
    sql = "select * from employees where id = 15"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    img = Image.open(io.BytesIO(result[0][4]))
    img = ImageTk.PhotoImage(img)
    l2 = tk.Label(root, image = img)
    l2.place(x = 0, y = 0)    
    l2.image = img
photoview()
root.mainloop()