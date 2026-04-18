import sqlite3

con = sqlite3.connect("data.db")

cursor = con.cursor()

# cursor.execute("create table student (id int primary key,name varchar(20),age int,address varchar(20))")

print("data sucessfuly add")

# cursor.execute("insert into student values(1,'rana',20,'surat')")
# cursor.execute("insert into student values(2,'harshada',21,'kosamba')")
# cursor.execute("insert into student values(3,'harsh',23,'rajakot')")
# cursor.execute("insert into student values(4,'harsil',24,'dubai')")
# cursor.execute("insert into student values(5,'harish',25,'jamnagr')")

con.commit()

cursor.execute("select * from student")
rows=cursor.fetchall()

print("Studemt Records:")
for i in rows:
    print(i)

con.close()