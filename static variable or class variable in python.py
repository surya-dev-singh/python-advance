# class variable are the variable whose single copy is available to all the instance of the class.
#if we modify the copy of class variable in an instance, it will affect all the copies in the other instance.

class Mobile(object):
    fp="yes" #this is class variable.
    def __init__(self):
        self.model="realme X"

    def show_model(self):
        print(self.model)
    
realme=Mobile()
    
#---------accessing class/static variable-----------------

#1. with class method.------------->

#to access class variable , we need class method with cls as first parameter then we can acess class variable using cls.variable_name

# eg:

class Mobile1(object):
    fp="yes" #class variable/static varible
    def __init__(self): #constructor
        self.model="realme x" #instance variable
    def show_model(self): #instance method
        print(self.model) #acessing instance variable
    @classmethod #class method decorator
    def is_fp(cls): #class mthod
        return  cls.fp #accessing class variable inside class method.

#2. accesing class/static variable outside the class----->

#we can access class variable using classname.variable_name
# eg:
print(Mobile1.fp)

#to access class method also we have to use classname.class_method()
print(Mobile1.is_fp())

#NOTE we can also acess class/static variable using object_name.variable_name(we will learn about it in detail while studying namespace topic)