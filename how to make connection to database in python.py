
#connect() : this method is used to open or establish a new connection . It returns an object representing the connection. 

#syntax : 

#connection_object = connect(user="username", password="pass",database="dbname",host="localhost",port=3306)

import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "database":"world",
    "host":"127.0.0.1",
    "port":3306
}
try:
    conn=mysql.connector.connect(**config)
    print("connection succeded!!")
    print("------------------------")
except:
    print("unable to connect")
    print("try checking your credential !!")
myc=conn.cursor()
query="SHOW TABLES;"
myc.execute(query)
for i in myc:
    print(i)
myc.close()
conn.close()

