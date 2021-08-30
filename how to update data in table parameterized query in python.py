import mysql.connector
try:
    conn=mysql.connector.connect(
        user="root",
        password="anything@123",
        host="localhost",
        database="pdb",
        port=3306
    )
    if(conn.is_connected()):
        print("connection successful")
except:
    print("unable to connect to mysql")
sql='update student set fees=%s where stuid=%s'
myc=conn.cursor()
f=float(input("enter the new fees : "))
sid=int(input("enter the new stuid  : "))
try:
    myc.execute(sql,(f,sid))
    conn.commit()
    print(myc.rowcount , 'row updated !')
except:
    conn.rollback()
    print("unable to update data ")
myc.close()
conn.close()


#similarly for dictionary !!


# sql='update student set fees=%(f)s where stuid=%(id)s'
# myc=conn.cursor()
# fee=float(input("enter the new fees : "))
# sid=int(input("enter the new stuid  : "))
# try:
#     myc.execute(sql,{'f': fee , 'id' : sid})
#     conn.commit()
#     print(myc.rowcount , 'row updated !')
# except:
#     conn.rollback()
#     print("unable to update data ")
# myc.close()
# conn.close()