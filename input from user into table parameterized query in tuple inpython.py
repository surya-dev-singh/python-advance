import mysql.connector
from termcolor import colored
config={
    "user": "root",
    "password": "anything@123",
    "host": "localhost",
    "database":"pdb"
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("----------------------------------------")
        print(colored("[+] mysql connected !!","green"))
except:
    print("unable to connect to mysql")

sql= "INSERT INTO student(name,roll,fees) VALUES (%s,%s,%s)"
myc=conn.cursor()
#input form user :
print("----------------------------------------")
nm=input(colored("ENTER THE NAME : ","cyan"))
print("----------------------------------------")
ro=int(input(colored("ENTER THE ROLL NO. : ","cyan")))
print("----------------------------------------")
fe=float(input(colored("ENTER THE FEES : ","cyan")))
print("----------------------------------------")
params=(nm,ro,fe)
try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount , colored("row inserted !!","green"))
    print("")
    print(colored(f"stu id : {myc.lastrowid} inserted !!","green"))
except:
    conn.rollback()
    print("unable to insert data !!")
myc.close()
conn.close()







