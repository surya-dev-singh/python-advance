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
params=[
        {'n':'anonymous','r':500,'f':604499},
        {'r':430,'n':"rohit sharma",'f':329209},
        {'n':"patrick",'r':330,'f':33922}
        ]
try:
    myc.executemany(sql,params)
    conn.commit()
    print(myc.rowcount," rows inserted !!")
    print(f"STUID :{myc.lastrowid}  -  {myc.lastrowid + myc.rowcount}  inserted !!")
except:
    conn.rollback()
    print("unable to insert data !!")
myc.close()
conn.close()

