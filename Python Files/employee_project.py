from tkinter import PhotoImage, filedialog, messagebox, END
import mysql.connector as mql
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io

def project():

    def add():
        emp_id = e1.get()
        emp_name = e2.get()
        emp_phone = e3.get()
        emp_sal = e4.get()

        mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
            )
        print("Data connected successfuly.")
        cursor = mydb.cursor()
        sql = "insert into employees (id, emp_name, emp_phone, emp_sal, image) values (%s,%s,%s,%s,%s)"
        val = (emp_id, emp_name, emp_phone, emp_sal, file)
        cursor.execute(sql, val)
        mydb.commit() 
        mydb.close()
        print("Data inserted successfully.")
        messagebox.showinfo("Information", "Employee Inserted Successfully...")
        show()
        photoview()
    def show():
        mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
        )
        print("Data connected successfuly.")
        cursor = mydb.cursor()
        sql = "select id, emp_name, emp_phone, emp_sal from employees"

        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        
        print("Data shown successfully.")
        clear_treeview()
        for i, (id, emp_name, emp_mob, emp_sal) in enumerate(result, start = 1):
            listbox.insert("", "end", values=(id, emp_name, emp_mob, emp_sal))
            mydb.close()
    def delete():
        emp_id = e1.get()
        mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
        )
        print("Data connected successfuly.")
        cursor = mydb.cursor()
        sql = "delete from employees where id = %s "
        val = (emp_id,)
        cursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Information", "Record Deleted Successfully...")
        show()
    def searchid():
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        emp_id = e1.get()
        mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
        )
        
        print("Data connected successfuly.")
        cursor = mydb.cursor()
        sql = "select id, emp_name, emp_phone, emp_sal, image from employees where id = %s"
        val = (emp_id,)
        cursor.execute(sql, val)
        records = cursor.fetchall()
        e2.insert(0, records[0][1])
        e3.insert(0, records[0][2])
        e4.insert(0, records[0][3]) # discuss
        print(records)
        photoview()
        messagebox.showinfo("Information", "Records Found")
    def searchname():
        e1.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        
        emp_name = e2.get()
        mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
        )
        
        print("Data connected successfuly.")
        cursor = mydb.cursor()
        sql = "select id, emp_name, emp_phone, emp_sal, image from employees where emp_name = %s"
        val = (emp_name,)
        cursor.execute(sql, val)
        records = cursor.fetchall()
        e1.insert(0, records[0][0])
        e3.insert(0, records[0][2])
        e4.insert(0, records[0][3]) 
        print(records)
        photoview()
        messagebox.showinfo("Information", "Records Found")
    def update():
        emp_id = e1.get()
        emp_name = e2.get()
        emp_mob = e3.get()
        emp_sal = e4.get()
        mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        
        )
        print("Data connected successfuly.")
        cursor = mydb.cursor()
        sql = "update employees set emp_name = %s, emp_phone = %s, emp_sal = %s where id = %s"
        val = (emp_name, emp_mob, emp_sal, emp_id)
        cursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Information", "Data Updated...")
        print("Data Updated Succesfully.")
        show()
    
    def clear_treeview():
        for i in listbox.get_children():
            listbox.delete(i) 
    def get_value(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        rowid = listbox.selection()[0]
        select = listbox.set(rowid)
        e1.insert(0, select["emp_id"])
        e2.insert(0, select["emp_name"])
        e3.insert(0, select["emp_mob"])
        e4.insert(0, select["emp_sal"])
        photoview()
    def sort():
        mydb = mql.connect(
        host = "localhost",
        database = "employee",
        user = "root",
        password = "4JVkrk75Jamd"
        )

        cursor = mydb.cursor()
        sql = "select id, emp_name, emp_phone, emp_sal from employees order by emp_name"
        cursor.execute(sql)
        result = cursor.fetchall()
        clear_treeview()
        for i, (id, emp_name, emp_mob, emp_sal) in enumerate(result, start = 1):
            listbox.insert("", "end", values=(id, emp_name, emp_mob, emp_sal))
            mydb.close()
    def photo():
        emp_id = e1.get()
        emp_name = e2.get()
        emp_phone = e3.get()
        emp_sal = e4.get()
        def convert_to_bd(filename):
            with open(filename, "rb") as file:
                bd = file.read()
            return bd
        path = filedialog.askopenfilename(initialdir="/",filetypes=((("Text files", "*.txt*"), ("all files", "*.*"))))
        print(path)
        file = convert_to_bd(path)
        print(file)
        mydb = mql.connect( 
                            host = "localhost",
                database = "employee",
                user = "root",
                password = "4JVkrk75Jamd"
                
                    )
        print("Data connected successfuly.")
        cursor = mydb.cursor()
        sql = "update employees set emp_name = %s, emp_phone = %s, emp_sal = %s, image = %s where id = %s"
        val = (emp_name, emp_phone, emp_sal, file, emp_id)
        cursor.execute(sql, val)
        mydb.commit() 
        photoview()
    def photoview():
        global l2

        emp_id = e1.get()
        mydb = mql.connect(
            host = "localhost",
            database = "employee",
            user = "root",
            password = "4JVkrk75Jamd"
            )
        cursor = mydb.cursor()
        sql = "select * from employees where id = %s"
        val = (emp_id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        print(result)
        img = Image.open(io.BytesIO(result[0][4]))
        img1 = img.resize((100,100),Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img1)
        l2 = tk.Label(root, image = img2)
        l2.place(x = 300, y = 50)   
        l2.image = img2
    def selectpic():
        global file
        def convert_to_bd(filename):
            with open(filename, "rb") as file:
                bd = file.read()
            return bd
        path = filedialog.askopenfilename(initialdir="/",filetypes=((("Text files", "*.txt*"), ("all files", "*.*"))))
        print(path)
        file = convert_to_bd(path)
    def clear():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        l2.after(0, l2.destroy())

    root = tk.Tk()
    root.geometry("800x500")
    root.title("Registration Form")
    root["bg"] = "black" 
    l1 = tk.Label(root, text = "REGISTRATION FORM", font = ("Times", 14, "bold", "underline"), bg = "#636363")
    l1.place(x = 300, y = 5)

    l22 = tk.Label(root, text = "1) Employee ID", bg="#636363").place(x = 10, y = 50)

    e1 = tk.Entry(root)
    e1.place(x = 140, y = 50)

    l3 = tk.Label(root, text = "2) Employee Name", bg = "#636363").place(x = 10, y = 90)

    e2 = tk.Entry(root)
    e2.place(x = 140, y = 90)

    l4 = tk.Label(root, text = "3) Mobile Number", bg = "#636363").place(x = 10, y = 130)

    e3 = tk.Entry(root)
    e3.place(x = 140, y = 130)

    l5 = tk.Label(root, text = "4) Salary", bg = "#636363").place(x = 10, y = 170)

    e4 = tk.Entry(root)
    e4.place(x = 140, y = 170)

    b1 = tk.Button(root, text = "Add", command = add, height=1, width=12, bg="#636363").place(x = 30, y = 210)

    b2 = tk.Button(root, text = "Delete", command = delete, height=1, width=12, bg="#636363").place(x = 130, y= 210)

    b3 = tk.Button(root, text = "Search by ID", command = searchid, height=1, width=12, bg="#636363").place(x=230, y= 210)

    b4 = tk.Button(root, text = "Search by Name", command = searchname, height=1, width=12, bg="#636363").place(x=330, y=210)

    b5 = tk.Button(root, text = "Update Data", command=update, height=1, width = 12, bg="#636363").place(x=430, y = 210)

    b6 = tk.Button(root, text = "Clear", command = clear, height = 1, width = 12, bg="#636363").place(x = 530, y = 210)

    b7 = tk.Button(root, text = "Sort", command = sort, height = 1, width = 15, bg = "#636363").place(x = 630, y = 210)

    b8 = tk.Button(root, text = "Update Photo", command = photo, height = 1, width = 15, bg = "#636363").place(x = 630, y = 210)

    b9 = tk.Button(root, text = "5) Select Picture", command = selectpic, height = 1, width = 15, bg = "#636363").place(x = 290, y = 170)
    colum = ("emp_id", "emp_name", "emp_mob", "emp_sal")



    listbox = ttk.Treeview(root, columns=colum, show = "headings")
    vsb = ttk.Scrollbar(root, orient = "vertical", command = listbox.yview)
    vsb.place(x = 785, y = 250, height = 200 + 20)
    # vsb.pack(side = "right", fill = "y")  
    listbox.configure(yscrollcommand=vsb.set)
    for call in colum:
        listbox.heading(call, text = call)
        listbox.grid(row = 1, column = 0, columnspan=2)
        listbox.place(x = 10, y = 250)

    show()
    listbox.bind('<Double-Button-1>', get_value)
    root.mainloop()



def check_info():
    username = ee1.get()
    password = ee2.get()
    real_password = "abc"
    real_username = "def"
    password_correct = False
    if username == real_username:
        username_correct = True
    if password == real_password:
        password_correct = True
    if username_correct and password_correct:
        messagebox.showinfo("Information", "Correct Username and Password")
        root_1.destroy()
        project()
        
    else:
        messagebox.showinfo("Information", "Username/Password Incorrect")
        exit()
    



root_1 = tk.Tk()
root_1.geometry("800x500")
root_1.title("Login Page")
root_1["bg"] = "black"
ll1 = tk.Label(root_1, text = "Login Page", font = ("Times", 14, "bold", "underline"), bg = "#636363").place(x = 300, y = 5)

ll2 = tk.Label(root_1, text = "Username", bg = "#636363").place(x = 10, y = 50)

ee1 = tk.Entry(root_1)
ee1.place(x = 140, y = 50)

ll3 = tk.Label(root_1, text = "Password", bg = "#636363").place(x = 10, y = 90)

ee2 = tk.Entry(root_1, show = "*")
ee2.place(x = 140, y = 90)
bb1 = tk.Button(root_1, text = "Submit", command = check_info, height=1, width=12, bg = "#636363").place(x = 30, y= 210)
image_1 = tk.PhotoImage(file = r"C:\Users\User\OneDrive\Documents\GitHub\employee-db\Python Files\hi2.png")
l4 = tk.Label(image = image_1)
l4.place(x = 400, y = 100)
l5 = tk.Label(root_1, text = "Ashank Project Work", fg = "black").place(x = 400, y = 300)
root_1.mainloop()

