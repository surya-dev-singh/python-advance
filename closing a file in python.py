# close() - This method is used to close, opened file. 

#once we close the file. file object is deleted from the memory hence file will be no longer accesible unless we open it again.

#if you don't explicitly close a file, python's garbage collector will eventually destroy the object and close the open file for you, but the file stay open for a while so you should always close opened file.

#what will happened if we do not close opened file: -
# ----> data of the file may be corruped or deleted.
#-----> memory utilized by the file  is not  freed it may cause of insufficient memory.


f=open("student.txt")
#opneration

f.close()
