#insert single row  -  dictionary
import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "host":"localhost",
    "database":"pdb",
    "port":"3306"
    }
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("connection successfull !")
except:
    print("unable to database !!")

q="INSERT INTO student(name,roll,fees) VALUES(%(n)s,%(r)s,%(f)s)"
myc=conn.cursor()
try:
    myc.execute(q,{'n':'piyush', 'r': 777 ,'f': 540000 }) # we can assign this dictionary  into some variable also !!
    conn.commit()
    print(myc.rowcount ," row added !!")
    print(f'stuid : {myc.lastrowid} inserted !!')
except:
    conn.rollback()
    print('unable to insert data !!')
myc.close()
conn.close()
