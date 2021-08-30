# pickling :  

#pickling is a process of converting a class object into a byte stream so that it can be stored into a file.This is a object serialization.
#we use pickle module to perform pickling and unpickling.


#functions :

#dump() : This function is used to perform the pickling . It returns the pickled representation of the object as a bytes object, instead of writing it to a file. This method belongs to pickle module. 
#syntax :
# import pickle
# pickle.dump(object,file)



#unpickling  : 

#unpickling is a process where byte stream is converted back into a class object. It is inverse operation of pickling. This is also called de-serialization.
#pickling and unpickling should be done using binary files since they support byte streams.
#we use pickle module to perform pickling and unpickling.

###WARNING : The pickle module is not secure againts erroneous or maliciouly constructed data. Never unpickle data recived from an untrusted or unautheticated source. 


#function :

#load() : this function is used to read an pickled object from a binary file and returns it into object. This method belongs to pickle module.
#syntax :
# import pickle
# pickle.load(file)


#---------------------------------------------------------------------

#why do we need pickling and unpickling  :

#when we store some structured data in the file and want to perform calculation that time we need pickling and unpickling.


#-----------------------------------------------------------------------


import pickle
class Student(object):
    def __init__(self, name , roll, address):
        self.name=name
        self.roll=roll
        self.address=address
    def disp(self):
        print(f"Name: {self.name} ROLL : {self.roll} address : {self.address}")

with open("pick.dat", mode="wb") as f :
    stu1=Student("Rahul",101,"ranchi")
    stu2=Student("surya",102,"gandhidham")
    pickle.dump(stu1,f)
    pickle.dump(stu2,f)
    print("pickling done !!!")

with open("pick.dat","rb") as f:
    obj1=pickle.load(f)
    obj2=pickle.load(f)
    print("unpickling done !!")
    obj1.disp()
    obj2.disp()