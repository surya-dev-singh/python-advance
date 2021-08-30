#operations : 

#create table
#show table
#insert data

#commint() method :
#this method is used to save inserted row in the table. It is required to make the changes, otherwise no changes are made to the table.

#This method sends a COMMIT statement to the MYSQL server, commiting the current transaction . Since by default connector/Python does not autocommit , it is important to call this method after every transaction that modifies data for tables that use transactional storage engines.
# syntax : connection_object.commit()
#eg : conn.commit()


#rollback() method:
# this method is used to un-save row(undo) , if ther is an error in sql query and we commited that.

#this method sends a ROLLBACK statement to the mysql server , undoing all data changes from the current transaction. by default , connector/python does not autocommit, so it is possible to cancel transactions when using transactional storage engines such as InnoDB.
#syntax : connection_object.rollback()
#eg:conn.rollback()

import mysql.connector
config={
        "user":"root",
        "password":"anything@123",
        "host":"127.0.0.1",
        "database":"pdb",
        "port":3306
        }
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("----------------------------------")
        print("connection to mysql successfull !!")
        print("----------------------------------")
except:
    print("unable to connect , please try again !!")

sql="SHOW TABLES"
myc=conn.cursor()
myc.execute(sql)
for i in myc:
    print(i)
print("------------------------------")
try:
    q="INSERT INTO student(name,roll,fees) VALUES('SUMIT',101,10000.53)"
    myc.execute(q)
    conn.commit()
    print("data insertion done successfully !!")
except:
    conn.rollback()
    print("unable to insert data !!")
myc.close()
conn.close()