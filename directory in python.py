# os module - This module is used to perform simple operation on directories.This module represents operating system dependent functionallity.
#syntax : import os

# functions:--

#1. getcwd() : This method is used to know the currently working directory.
#syntax : os.getcwd()
 
#2. mkdir("dirname") : this method is used to create a directory in the present directory
#syntax : os.mkdir("dirnmae")

#3. mkdir("parentdirname/childdirname") : This method is used to create a child directory in the parent directory. parent directory must be exist else it will show error.
#syntax : os.mkdir("parentdirname/childdirname")

#4. makedirs("parentdir/childdir/grandchilddir") : this method is used to recursively create sub directories.
#syntax : os.makedirs("parentdir/childdir/grandchilddir")

#5. chdir("dirname") : this method is used to change current working directory.
#syntax : os.chdir("dirname")

#6. rename("oldname","newname") : this method is used to change the directory name.
#syntax : os.rename("oldname","newname")

#6. rmdir("dirname") : this method is used to remove a directory from the current working directory . we can also specify path for directory.
#synatx : os.rmdir("dirname") , os.rmdir("parentdirname/childdirname")

#7. removedirs("dirname") : this method is used to recursicely remove all direcotories.break
#syntax : os.removedirs("parentdirname/chidldirename")

#8.walk():  this method is used to know contents of a directory including sub directory. it returns an iterator object whose contents can be displayed using for loop. This iterator object contains direcotory path , direcotyname, filename found in the specified directory.
#syntax : os.walk(path,topdown=True,oneerror=None,followlinks=False)

import os
for i in  os.walk("."):
    print(i)
