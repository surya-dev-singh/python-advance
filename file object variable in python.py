# file object variable :-

#name - This shows the name of specified file.
#syntax:- file_object.name

#mode - This shows mode(purpose) of the file.
#syntax:- file_object.mode

#closed - this used to check wheter file has closed or not.
#it shows True if file is closed else shows False.
#syntax: file_object.closed


#file object method :-

#readable() - This method is used to check whether file is readable or not.
#it return True if file is readable else returns False.
#syntax : file_object.readable()

#writeable() - This method is used to check whether file is writable or not .
#this return True if file is writable else returns False.
#synatx : file_object.writable()
 
f=open("student.txt", mode='r') #make sure you have a filename that is specified , to read in r mode.
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)