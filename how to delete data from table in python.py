import mysql.connector
try:
    conn=mysql.connector.connect(
        user="root",
        password="anything@123",
        host="localhost",
        database="pdb",
        port="3306"
    )
    if (conn.is_connected()):
        print("------------------------")
        print("connection successful !!")
        print("------------------------")
        print("#########################")
        print("#                       #")
        print("#       welcome         #")
        print("#                       #")
        print("#########################")
except:
    print("----------------------")
    print("unable to connect !!! ")
    print("----------------------")
q="DELETE FROM  student WHERE stuid=6"
myc=conn.cursor()
try:
    myc.execute(q)
    conn.commit()
    print("data manupulation take place successfully !!")
    print("--------------------------------------------")
    print(myc.rowcount ," row deleted successfully !!")
except:
    print("unable to modify the sql data !!")
    print()
    conn.rollback()
    
myc.close()
conn.close()

