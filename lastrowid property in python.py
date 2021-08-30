#This read-only property returns the value generated for an AUTO_INCREMENT column by the privious INSERT or UPDATE statement or None when there is no such value available.
#if you perform an INSERT into a table that contains an AUTO_INCREMENT column, lastrowid returns the AUTO_INCREMENT value for the new row.
#if you insert multiple rows into a table using single INSERT statement, the lastrowid property contains the last insert id of the first row.
#curor_object.lastrowid
#eg: myc.lastrowid

import mysql.connector
conn=mysql.connector.connect(user="root",password="anything@123",host="localhost",database="pdb")
try:
    if conn.is_connected():
        print("connection successfull !")
except:
    print("unable to connect to mysql")
try:
    q="INSERT INTO student(name,roll,fees) VALUES ('root', 391 ,2938.45)"
    myc=conn.cursor()
    myc.execute(q)
    conn.commit()
    print(myc.lastrowid)
except:
    print("getting error in inserting values")
    conn.rollback()
myc.close()
conn.close()