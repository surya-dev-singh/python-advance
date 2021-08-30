#user defined exception :

# a programmer can create his own excepitons , called user-defined exceptions or custom exception.

# creating exception class using exception class as base class.
# raising exception
# handling exception


#---------------------------------------------------------------------------------------
#creating exception:

# we can create our own exception by creating a sub class to built-in exceptions class.

#eg :
# class MyException(Exception):
    # pass

#eg:
# class MyException(Exception):
#     def __init__(self,arg):
#         self.msg=arg

#-----------------------------------------------------------------------------------------
#raising exception:

#raising exception is used to raise the user defined exception.
# raise MyException("message")

#-----------------------------------------------------------------------------------------
#handling exception:

#using try and block programmer can handle exceptions.
# try:
    # statement
# except MyException as myek:
#   stement

# ----------------------------------------------------------------------------------------

# note : there is namming convention that when you are defining user defined exception class try to put Error at the end.

class BlanceExceptionError(Exception):
    pass

def checkbalance():
    money=10000
    withdraw=9000
    try:
        balance=money-withdraw    
        if(balance<=2000):
            raise BlanceExceptionError("Insufficient Balance") #this message will be passed to except block's "be" variable , and it will be shown there !! 
        print(balance)
    except BlanceExceptionError as be:
        print(be)
checkbalance()