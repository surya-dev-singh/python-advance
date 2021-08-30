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

sql="select * from city where name=%s"
myc=conn.cursor()
c=input("enter the name of city : ")
try:
    myc.execute(sql,(c,))
    row=myc.fetchone()
    print(row)
    print('total row : ' , myc.rowcount)
except:
    print("unable to retrive data !!")
myc.close()
# conn.close()

#similary for dict :

# sql="select * from city where name=%(name)s"
# myc=conn.cursor()
# c=input("enter the name of city : ")
# try:
#     myc.execute(sql,{"name":c})
#     row=myc.fetchone()
#     print(row)
#     print('total row : ' , myc.rowcount)
# except:
#     print("unable to retrive data !!")
# myc.close()
# conn.close()

