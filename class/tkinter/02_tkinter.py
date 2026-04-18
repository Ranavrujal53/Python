from tkinter import *
import mysql.connector as sql

con=sql.connect(
    host = "localhost",
    port = 3306,
    username = "root",
    password = "rana",
    database = "vru12"
)

coursor = con.cursor()


root = Tk()
root.geometry("700x600")
root.title("APP")
def add():
    name = t1.get()
    password = t2.get()
    address = t3.get()
    pincode = t4.get()
    coursor.execute(f"insert into data(name,password,address,pincode) values('{name}','{password}','{address}','{pincode}') ")

    con.commit()
    print("Data inserted successfully")

    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)

l1 = Label(root,text="name").place(x=300,y=200)
l2 = Label(root,text="password").place(x=300,y=250)
l3 = Label(root,text="address").place(x=300,y=300)
l4 = Label(root,text="pincode").place(x=300,y=350)

t1=Entry(root)
t1.place(x=400,y=200)
t2=Entry(root)
t2.place(x=400,y=250)
t3=Entry(root)
t3.place(x=400,y=300)
t4=Entry(root)
t4.place(x=400,y=350)

b1 = Button(root,text="Submit",width=20,command=add).place(x=400,y=450)
root.mainloop()