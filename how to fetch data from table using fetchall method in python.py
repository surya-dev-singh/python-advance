#fetch() method :
#This method fetches all(or remaining ) rows of a query result set and returns a list of tuples. If no more rows are available , it returns an empty list. you must fetch all rows for the current query before executing new statements using same connection.
# syntax : rows=cursor_object.fetchall()
import mysql.connector
try:
    conn=mysql.connector.connect(
        user="root",
        password="anything@123",
        host="127.0.0.1",
        database="world",
        port=3306
    )
    if(conn.is_connected()):
        print("CONNECTION SUCCESSFULL !!")
except:
    print("unable to connect")

sql="SELECT * from city;"
myc=conn.cursor()
try:
    myc.execute(sql)
    rows=myc.fetchall() #if we have already fetch some data earlier , then this method will only fetch the remaining.
    for r in rows:
        print(r)
    print("###################")
    print("total rows",myc.rowcount)
except:
    conn.rollback()
    print("unable to fetch data")
myc.close()