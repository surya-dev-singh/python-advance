#fetchone() method:

# This method returns one record as a tuple, If there are no more records then it returns None.

#This method retrives the next row of a query result set and returns a single sequence , or None if no more rows are availabel. By default , the returned tuple consists fo data returned by the MYSQL server, converted to python objects. if the cursor is a raw , no such conversion occurs.

#you must fetch all rows for the current query before executing new statements using the same connection.

#syntax : row=cursor_object.fetchone()
#eg : row=myc.fetchone()

import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "host":"localhost",
    "port":3306,
    "database":"world"
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("connection to mysql successfull !!")
except:
    print("unable to connect to mysql !!")
q="SELECT * FROM city"
myc=conn.cursor()
try:
    myc.execute(q)
    row=myc.fetchone()
    while row is not None:#we have to fetch all rows until it become non
        ID=row[0]
        NAME=row[1]
        COUNTRY_CODE=row[2]
        DISTRICT=row[3]
        POPULATION=row[4]
        print("##################################################")
        print(f"ID = {ID}")
        print(f"NAME = {NAME}")
        print(f"COUNTRY CODE = {COUNTRY_CODE}")
        print(f"DISTRICT = {DISTRICT}")
        print(f"POPULATION = {POPULATION}")
        row=myc.fetchone() #will fetch the next query 
    #------------------------------------
    # we can also do the above like this:
    # for i in myc:
    #     print(i)
    #----------------------------------
    # conn.commit() // no need of it because no dml work.
    print("---------------------------------------------")
    print(myc.rowcount , "fetched rows")
    print("---------------------------------------------")
except:
    print("unable show data !!")
    conn.rollback()
myc.close()
conn.close()