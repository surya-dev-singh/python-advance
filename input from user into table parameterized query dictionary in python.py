import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "database":"pdb",
    "host":"localhost"
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("connection successfull !!")
except:
    print("unable to connect to database !!")
var="name,roll,fees"
sql=f"INSERT INTO student({var} )"  + "VALUES (%(n)s,%(r)s,%(f)s)"
print(sql)
myc=conn.cursor()
#data input from user
nm=input("enter the name : ")
ro=int(input("enter the roll : "))
fe=float(input("enter the fees : "))
params={"n":nm,"r":ro,"f":fe}
try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount," rows inserted !!")
    print(f"STUID : {myc.lastrowid} inserted !!")
except:
    conn.rollback()
    print("unable to insert data !!")
myc.close()
conn.close()


#similarly we can use it to insert more than one data , for that we have to every time call a function that will insert data in database, when user gives the data, after insertion , program should prompt , whether to exit or not, we can achive this senerio using ifinite loop using while.
