import mysql.connector as sql

con =sql.connect(
    host = "localhost",
    port =3306,
    user = "root",
    password = "rana",   
    database = "vru12"
)

cursor = con.cursor()

# cursor.execute("create database vru12")

# cursor.execute("create table animal(id int primary key,animal_name varchar(50),type_of_animal varchar(50))")

# cursor.execute("insert into animal values (1,'dog','pet animal')")
# cursor.execute("insert into animal values (2,'lion','whild animal')")
# cursor.execute("insert into animal values (3,'camel','pet animal')")
# cursor.execute("insert into animal values (4,'tiger','whild animal')")

con.commit()