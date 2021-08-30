#operations :

#create table
#show table

import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "host":"localhost",
    "port":3306,
    "database":"pdb"
}
try:
    conn=mysql.connector.connect(**config)
    if (conn.is_connected()):
        print("connection")
except:
    print("unable to connect !!")

sql="CREATE TABLE student(stuid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) ,roll INT, fees FLOAT)"
myc=conn.cursor()
myc.execute(sql)
myc.execute("SHOW TABLES")
for i in myc:
    print(i)
myc.close()
conn.close()