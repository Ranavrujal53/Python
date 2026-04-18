import sqlite3

con = sqlite3.connect("mydatabase.db")

cursor = con.cursor()

cursor.execute("create table studnet(id int primary key,name varchar(20),age int)")

print("Database and table create successfully")

con.close()