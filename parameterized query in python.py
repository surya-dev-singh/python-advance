#a parameterized qruery is a query in which a query which can use the format or pyformat paramererization stylle for parameter and the parameter values supplied at execution.
#these executed with mysql cursor can use the %s and %(key)s format style.
#%s is used as format style in the sql queires, while using tupel parameter.
#%(key)s is used as format style in the sql queries , while using dictionary parameters.

#myc=conn.cursor()

#----------tuple parameters-----------
#eg :
# sql='INSERT INTO STUDENT(name,roll,fees)values(%s%s%s)'
# myc=conn.cursor()
# myc.execute(sql,("rohan",111,"6000.40"))
#now rohan,111,6000.40 will pass to placeholder %s ,in our sql query.

#-------------dictionary parameters-------
# sql='INSERT INTO student(name,roll,fees) VALUES(%(name)s,%(roll)s,%(fees)s)'
# myc=conn.cusor()
# myc.execute(sql,{'name':'surya','roll':777,'fees':54100})

#------------------------------------------------------------------------
import mysql.connector
from termcolor import colored
try:
    conn=mysql.connector.connect(
        user='root',
        password='anything@123',
        host="localhost",
        database='pdb',
    )
    if(conn.is_connected()):
        print(colored("----------------------------","yellow"))
        print(colored("[+]","green"),"connection to mysql successfull !!")
        print(colored("-----------------------------","yellow"))
except:
    print("unable to connect to mysql !!")

sql='INSERT INTO student(name,roll,fees) VALUES(%s,%s,%s)'
myc=conn.cursor()
try:
    myc.execute(sql,("sumit",106,6000))
    print(colored(f"{myc.lastrowid} inserted","green"))
    conn.commit()
except:
    conn.rollback()
    print("error in inserting value ")
myc.close()
conn.close()

