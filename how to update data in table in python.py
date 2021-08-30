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
    if(conn.is_connected()):
        print("connection to mysql successfull !!")
except:
    print("unable to connect to mysql !!")
q="UPDATE student SET fees=3000 WHERE stuid=2"
myc=conn.cursor()
try:
    myc.execute(q)
    conn.commit()
    print(myc.rowcount , "row has been updated !!")
except:
    print("unable to perform DML on sql !!")
    conn.rollback()
myc.close()
conn.close()