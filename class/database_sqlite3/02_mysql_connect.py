import mysql.connector as sql

con = sql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "rana",
    database = "rana12"

)
cursor = con.cursor()

# cursor.execute("CREATE DATABASE rana12")
# cursor.execute('create table student (id int primary key AUTO_INCREMENT,name varchar(50),email varchar(50),age int)')

cursor.execute(
"INSERT INTO student VALUES (1,'rana', 'rana12@gmail.com', 20)"
)
con.commit()



# print("connect")