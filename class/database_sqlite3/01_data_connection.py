import sqlite3

con = sqlite3.connect("data.db")

# qry = "create table student(id int primary key,name vatchar(20),email varchar(50)) "

# qry = "insert into student values(3,'vrujal','vrujal@123gmail.com')"

# qry = "update student set name ='rana vrujal' where id =2"

# qry = "delete from student where id = 1 "
 
# con.execute(qry)
con.commit()

# data = con.execute("select * from student")
# for i in data.fetchall():
#     print(i)

# con.execute("drop table student")