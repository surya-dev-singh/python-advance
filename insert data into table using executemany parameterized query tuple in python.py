#executemany() method : this method is used to prepare given sql query and execute it against all parameters sequences or mapping found in the sequence seq_of_params.

#with the executemany() method , it is not possible to specify multiple statements to execute in the sql arguments.

#syntax : cursor_object.executemany(sql,seq_of_params)
#sql= it is the query
#seq_of_params = it is a list of tuples, containing the data to insert. 
import mysql.connector
from termcolor import colored
config={
    "user":"root",
    "password":"anything@123",
    "host":"localhost",
    "port":"3306",
    "database":"pdb"
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected):
        print("---------------------------------------------")
        print(colored("connection to mysql successfull !!","yellow"))
        print("---------------------------------------------")
except:
    print(colored("unable to connect to mysql","red"))

sql="INSERT INTO student(name,roll,fees) VALUES(%s,%s,%s)"
myc=conn.cursor()
#inseat of writing whole list of tuples , we can make a variable like seq_of_param, then pass that to executemany.
try:
    myc.executemany(sql,[("jai",1011,4000.50),("raj",1012,5000.50),("kartik",1013,6000.60)])
    conn.commit()
    print(myc.rowcount,"row inserted !!")

except:
    conn.rollback()
    print("unable to insert data into database")

myc.close()
conn.close()
