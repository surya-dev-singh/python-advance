#mysql :
#it is an open source database management system application which will help us to manage the database like store and retrive data.
#to work with mysql in python program we have to import connector sub module of mysql module.

#syntax : import mysql.connector

#-----------------creating connection----------------------

#connect() : this method is used to open or establish a new connection. It returns an object representing the connection.

#syntax : 
# connection_object = connect(user="username" , password="pass", host="localhost", port=3306)

# import mysql.connector
# con=mysql.connector.connect(user="root",password="anything",host="localhost",port=3306)

#creating connection different way :

import mysql.connector
config={
    "user":"root",
    "password":"anything@123",
    "host":"127.0.0.1",
    "port":3306
}
conn=mysql.connector.connect(**config)
#**config means it is keyword argument ( it will send all data of dict as keyword agument in to connect function of connector submodule.)

#--------------------check connection--------------------------

#is_connected() : this method is used to check if the connection to mysql is established or not. It returns True if the connection is established successfully. 
#syntax : connection_object.is_connection()

print(conn.is_connected())


#-----------------------close connection--------------------------

#close() : this method is used to close the connection.
#syntax : connection_object.close()
conn.close()

