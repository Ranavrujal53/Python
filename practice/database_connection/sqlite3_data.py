import sqlite3

con =sqlite3.connect("data.db")

# qry = "create table student(id int primary key,name varchar(50),email varchar(50),age int)"

# qry = "insert into student values (1,'rama','rama12@gmail.com',20)"\

# qry = "update student set email='ram12@gmail.com' where id=1"

# con.execute(qry)
con.commit()

data = con.execute("select * from student")
for i in data.fetchall():
    print(i)
