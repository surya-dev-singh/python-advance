import mysql.connector
conf={
    "user":"root",
    "password":"anything@123",
    "host":"127.0.0.1",
    "database":"pdb",
    "port":3306
}
try:
    conn=mysql.connector.connect(**conf)
    if(conn.is_connected()):
        print("connection succesfull!!")
except:
    print("unable to connect !!")

sql = "SELECT * FROM student WHERE NAME='SURYADEV'"
myc=conn.cursor()
try:
    myc.execute(sql)
    row=myc.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()
except:
    conn.rollback()
    print("unable to fetch data !!")
myc.close()
conn.close()