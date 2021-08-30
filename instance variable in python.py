# type of variable :--

#1. instance variable.
#2. class variable/static variable.


#----------what are instance variable-----------------

#instance variables are the variables whose separate copy is created in every object.
#instance variable are defined and initialized using a constructor with self parameter.

#eg:
class Mobile:
    def __init__(self):
        self.model="realme z"  #this is instance variable.
    def show_model(self):
        print(self.model)
realme=Mobile()
print(realme.model)

#copy of each instance variable is created for every object of the class.


#------------accessing instance variable------------------

#1. with instance method(similar to method in class except __init__())

# in this we access instance variable inside the class.
#to access instance variable, we need instance method with self as first parameter then, we can access instance variable using sef.variable_name.
# eg:

class Mobile1(object):
    def __init__(self):
        self.model="realme x"  #instance variable
    def show_model(self): #instance method
        self.model #accessing instance variable.
realme=Mobile1()

#2. accessing instance variable outside the class.

#we can  access instnce variable using object_name.variable_name
print(realme.model)

#if we modify the copy of instance variable in an instance , it will nor effect all the copies in the other instance.