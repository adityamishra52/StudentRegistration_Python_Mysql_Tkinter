import mysql.connector

try:
    print("-"*100)
    cnx=mysql.connector.connect(host="localhost",user="root",password="1234",database="college")
    cur=cnx.cursor()
    query1="use college"
    cur.execute(query1)
    query2="show tables like 'student'"
    cur.execute(query2)
    result = cur.fetchone()
    if result is None:
        query3="create table student(id int AUTO_INCREMENT PRIMARY KEY,name varchar(30) not null, branch varchar(25) not null, photo BLOB )"
        cur.execute(query3)
    else:
        print("table already exixts")

    
except mysql.connector.Error as e:
    print("problem in your connection With My sql server",e)