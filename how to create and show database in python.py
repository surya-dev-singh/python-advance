#operations :
#create database
#show database

#cursor() method :

#This method is used to create cursor class object
#we need cursor object so we can call execute() method.
#syntax : cursor_object = connection_object.cursor()

#arguments may be passed to the cursor() method to control what type of cursor to create:
    #if buffered is True , the cursor fetches all rows from the server after an operation is executed . This is useful when queries return small result sets. buffered can be used alone, or in combination with the dictionary or named_tuple argument.
    #if dictionary is True, the cursor returns row as dictionaries.
    #if named_tuple is True, the cursor return rows as named tuples.
    #if prepared id true, the cursor is used for executing prepared statements.
    #if raw is True , the cursor skip the conversion from mysql data types to python types when fetching rows . A raw cursor is usually used to get better performance or when you want to do the conversion yourself.
    #The cursor_class arguments can be used to pass a class to use for instantiating a new cursor . it must be a subclass of cursor.CursorBase

#the return object depends on the combination of the arguments . examples :

#if not buffered and not raw then we will get object of this class: MYSQLCursor (class for cursor object)
#if buffered and not raw then we will get object of this class : MYSQLCursorBuffered (class for cursor object)
#if not buffered and raw then we will get object of this class : MYSQLCursorBufferedRaw (class for cursor object)
#if buffered and raw then we will get object of this class : MYSQLCursorBufferedRaw

# eg:
# myc = conn.cursor()
# myc = conn.cursor(buffered=True)
# myc=conn.corsor(prepared=True)


#execute() method :---------------------------

#this method is used to execute given sql queries.
#we need cursor object so we can call execute() method.
#syntax: cursor_object.execute(sql, param=None, multi=False) 
    #sql - it is sql query
    #param - The parameters found in the tuple or dictionary param are bound to the variables in the operation.
    #multi - execute() returns an iterator if multi is true .


#eg : 
# myc=conn.cursor()
# myc.execute("SELECT * FROM student")


#close() cursor : -----------------------------

#close() method closes the cursor, resets all result , and ensure that the cursor object has no reference to its original connection object.
#syntax : cursor_object.close()
#eg : myc.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import mysql.connector
config={
    "user" : "root",
    "password" : "anything@123",
    "host" : "127.0.0.1",
    "port" : 3306
}

try:
    conn=mysql.connector.connect(**config)
    if (conn.is_connected()):
        print("mysql server has been connected successfully !!!")
        print("------------------------------------------------")
        
except:
    print("we are getting some error in connecting to sql server")
    print("TRY CHECKING YOUR CREDENTIAL !")

myc = conn.cursor()
myc.execute("CREATE DATABASE pdb3")
myc.execute("SHOW DATABASES")
for d in myc:
    print(d)   
myc.close()
conn.close()

