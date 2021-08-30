#prepared statement :

# a prepared statement is used to execute the same statement repeatedly with high efficiency. 
# The prepared statement execution consits of two stages : prepare and execute.

#at the prepare stage a statement template is sent to the database server. the server perform a syntax check and initialize server internal resources for later use.

#at the execute stage the parameter values are sent to the database server . The server create a statement template and these values to execute it.

#prepated statement execute with MYSQLCursorPrepared can use the format %s or qmark ? parameter style.

# %s and ? are called as parameter marker.

# This differs from nonprepared statements executed with MySQLCursor, which can use the format or pyformat parameterization style.


#--------------------------------------------------------------------------------------

#ADVANTAGE:

# prepared statements are very useful against sql injections.
# prepared statements reduce parsing time as the preparation on the query is done only once (although the statements isn executed multiple times)

#---------------------------------------------------------------------------------------

#creating a Cursor()

#using prepared=True arguments to the cursor() method , creates a cursor that enables execution of prepared statements using the binary protocal.
# In this case, teh cursor() method of the connection object returns a MySQLCursorPrepared object.

# eg : myc=conn.cursor(preapred=True)

# sql="insert into student(name,roll,fess) values(?,?,?)"     #we can also use %s.
# myc=conn.cursor(preapred=True)
# myc.execute(sql,("rohan",111,1232424))

# note : for prepared statements , we can only pass parameter as tuple, we cannot use dictionary.

#-----------------------------------------------------------------------------------------

#HOW IT WORKS : 

#for the first call to the execute() method , the cursor prepares the statements. If data is given in the same call, it also executes the staement and you should fetch data.

# for subsequent execute() calls that pass the same sql statements, the cursor skips the preparation phase.

#----------------------------------------------------------------------------------------

import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "host": "localhost",
    "database":"pdb"
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("connection to mysql succssfull !!")
except:
    print("unable to connect to mysql")
sql="insert into student(name,roll,fees) values(?,?,?)"
myc=conn.cursor(prepared=True) #now myc is object of MySQLCursorPrepared() class
param=("sohan",112,65000) 
try:
    myc.execute(sql,param)
    conn.commit()
    print(myc.rowcount, "row inseted!! ")
    print(f"stud ID {myc.lastrowid} inserted !!")
except:
    conn.rollback()
    print("unable to insert data !!")
myc.close()
conn.close()

