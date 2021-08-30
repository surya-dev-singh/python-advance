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

sql="select * from city where CountryCode=%(cc)s"
myc=conn.cursor()
try:
    myc.execute(sql,{'cc':'IND'})
    row=myc.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()
    print("================================================")
    print("total rows: ",myc.rowcount)
    print("================================================")
except:
    print("unable to retirve data")
myc.close()
conn.close()