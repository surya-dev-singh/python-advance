import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "database":"world",
    "host":"localhost"
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("connection successfull !!")
except:
    print("unable to connect to database !!")

sql="select * from city where name=%(N)s"
myc=conn.cursor()
try:
    myc.execute(sql,{'N':"gandhidham"})
    row=myc.fetchone()
    print(row)
    print("total rows : ", myc.rowcount)
except:
    print("unable to retrive data")
myc.close()
conn.close()