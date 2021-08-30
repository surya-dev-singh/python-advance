#fetchmany() method.

#this method fetches the next set of rows of a query result and returns a list  of tuples .If no more rows are available, it returns an empty list. 
#the number of rows returned can be specified using size argument, which default to one. Fewer rows are returned if fewer row are available than specified.
#you must fetch all rows for the current query before executing new statments using the same connection.
#syntax : rows=cursor_object.fetchmany(size=1)
# eg : rows=myc.fetchmany(3) or size=3
import mysql.connector
config={"user":"root",
        "password":"anything@123",
        "host":"127.0.0.1",
        "database":"world",
        "port":3306}
try:
    conn=mysql.connector.connect(**config)
    if (conn.is_connected()):
        print("connection to mysql server successfull !!")
except:
    print("unable to connect to mysql server !!")
sql="SELECT * FROM CITY"
# myc=conn.cursor() # since we are retriving only five rows, then this will show error until we fetch all rows, now to overcome this we can use buffered cursor
myc=conn.cursor(buffered=True) # it will fetch all the rows behind the scene , you will not get error , but it will fetch all rows.
try:
    myc.execute(sql)
    rows=myc.fetchmany(size=5)
    for r in rows:
        print(r)
    #we can use below commented code if we have not used buffered cursor object , the fetchall() will retrive all remaining data.
    # rows=myc.fetchall()
    # for r in rows:
    #     pass


    print("-----------------------------------")
    print("total rows",myc.rowcount)
except:
    conn.rollback()
    print("unable to fetch data !!")
myc.close()
conn.close()



    