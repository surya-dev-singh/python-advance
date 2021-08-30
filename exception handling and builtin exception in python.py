#exception :

# an exception is a runtime error which can be handled by the programmer.
# all exceptions are represented as classes in python.


#type of exception:
    #built-in exception: exceptions which are already available in python language . The base class for all built-in excepttions is BaseException class.
    
    #user defined exception: a programmer can create his own exceptions, called user-difined exceptions.
"""
BaseException > Exception > Standard Error ,warining 

**standard error :
AirthmeticError
AssertionError
SyntaxError
TypeError
EOfError
RuntimeError
ImportError
NameError


**waring:
DeprecationWarning
RuntimeWarning
ImportWarning
""" 

#need of exception handling :
# when an exception occurs, the program terminates sudenly.
#suddenly termination of program may corrupt the program.
# exception may cause data loss from the database or a file.

#--------------------------------------------------------------------------------
# Exception handling

# try : the try block contains code which may cause exceptions.
# eg :
# try : 
#   statements
 

# except : the except block is used to catch an exception that is raised in the try block .There can be multiple except block for try block.
# eg : 
# except Exception name : 
    # statements 

# else : This block will get executed when no exception is raised. Else blocked is executed after try block.

#finally : This block will get executed irrespective of whether there is an exception or not.

#----------------------------------------------------------------------------------------

# we can write several except block for a single try block.
# we can write multiple except block to handle multiple exceptions.
# we can write try block without except block.  
# we cannot write except block without try block.
# finally block is always executed irrespective of whether there is an exception or not.
# else block is optional.
# finally block is optional. 
#-----------------------------------------------------------------------------------------

# except : 
#---> with the Exception Class Name:
# eg :

# except ExceptionClassName:
    # statements

#----> exception as object
#eg: 

#except ExceptionClassobject as obj:
#   statement

#-----> multiple exceptions with tuples
#eg: 

#exception (ExceptionClassName1,ExceptionClassName2,........):
#   statement

#----->catch any type of Exception
#eg: 

#except : 
#   statement

#---------------------------------------------------------------------------------------

# a=10
# b=0
# try:
#     d=a/b
#     print(d)
#     print("inside try")
# except ZeroDivisionError:
#     print("cannot divide number by zero")
# else:
#     print("inside else")
# finally:
#     print("rest of code")


#----------------------------------------------------------------------------------------

a=10
b=0
try:
    d=a/b
    print(d)
    print("inside try")
except ZeroDivisionError as obj:
    print(obj) #this will give small description about error
except NameError as ob:
    print(ob)
except:
    print("unknow error occur")
print("rest of the code")