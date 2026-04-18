import sqlite3

print("Program start")

con = sqlite3.connect("student.db")

cursor = con.cursor()

# cursor.execute("create table stud (id int primary key,name varchar(50),age int,address varchar(50))")

# cursor.execute("insert into stud values(1,'Rana',20,'kosamba')")
# cursor.execute("insert into stud values(2,'Meet',21,'Rajashthan')")
# cursor.execute("insert into stud values(3,'Raj',22,'kolakata')")
# cursor.execute("insert into stud values(4,'Harsh',25,'Gujarat')")
# cursor.execute("insert into stud values(5,'Sachin',30,'Bharuch')")

# con.commit()

cursor.execute("select * from stud")

rows = cursor.fetchall()

print("Student Record")
for i in rows:
    print(i)

con.close()
print("Program ended")

