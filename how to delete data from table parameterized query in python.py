import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    'database':'pdb'
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("connection to mysql successfull")
except: 
    print("unable to connect to mysql !!")
sql='delete from student where stuid=%s'
myc=conn.cursor()
try:
    del_value=tuple(input('ENTER THE STUID TO DELETE: '))
    myc.execute(sql,del_value)
    conn.commit()
    print(myc.rowcount,' row deleted !!')
except:
    conn.rollback()
    print('unable to delete data !!')
myc.close()
conn.close()    

#similarly we can use it for dictionary !!, just use %(id)s as parameter.