# this read-only property returns the number of rows returned for SELECT statements, or the number of rows affected by DML statements such as INSERT or UPDATE.
#SYNTAX : cursor_object.rowcount
#eg: myc.rowcount
import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "host":"127.0.0.1",
    "database":"pdb"
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("----------------------------------")
        print("connection to mysql successfull !!")
        print("----------------------------------")
except:
    print("unable to connect to mysql server, please try again !")

myc=conn.cursor()
q="INSERT INTO student(name,roll,fees) VALUES('DEV',1,39990.3)"
try:
    myc.execute(q)
    conn.commit()
    print(myc.rowcount, "ROW INSERTED !!")
    print("-----------------------------")
except:
    conn.rollback()
    print("unable to insert the data!!")
myc.close()
conn.close()