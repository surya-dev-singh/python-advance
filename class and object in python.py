# what is class ?
# a python class is a group of attribute and methods.

# what is attribute ? 
# attributes are represented by varible that contains data.

# what is method ? 
# method performs an action or task.It is similar to function. 

#--------------------------------------------------

# how to create class ? 

#syntax:
# 
# class Class_name(object):
#     def __init__(self):
#         self.varible_name=Value
#         self.variable_name='value'
#     def method_name(self):
        #body of method.




# here method_name and __init__ are both method , but __init__ is special type of method , it is actully constructor , where as method_name is gernal method just like function we are used to with.

# we need to pass self variablr to these method , many people think self is keyword of python but it is not , it is a variable.

#the variable_name are attributes, there are other places also where we make variable , which are also called as variables.

#we can pass an object in class of python , which is optional. means we can simply define a class without object like this ---->
# class new_class_name:
#     def __init__(self):
#         self.new_variable_name=Value
#         self.other_new_variable_name='value'
#     def method_name(slef):
        #body of method.


#class - class is keyword is used to create a class.

#object - object represent the base class name from where all classes in python are derived.this class which we make is also derived from object class. this is optional , means if we do not write object while defining our class , it will by default derived from object class.

#__init__() - this method(not actually) is used to initialize the variable. This is a special method . we do not call this method explicitly.

#self -self is a variable which refers to current class instance/object.

#class name should be start with capital letter(not neccessary).



#creating class

# class Mobile:
#     def __init__(slef):
#         self.model="Realme Z"
#     def show_model(self):
#         print("MODEL : ",model)

# the above is incomplete class, because there is no object.
#now look at this-->
# class Abc:        #not written (object) , it is optional.
#     def __init__(self):
#         self.variable_name=Value
#         self.variable_name="value"
    # def method_name(self):
        #body of method
    # def method_name(self,f1,f2): 
        #here f1 and f2 are parameter , we also called it as formal argument.
        #body of method.

#our method can have parameter, but first name should be self or the keyword which is carrying our object.

#our special mthod , __init__() can also have different parameter, but first parameter should be self, or the keyword which is carrying our object.

#the parameter we use in our special method __init__() , we can use those parameter in that method. and the parameter we have define in our gernal method , we can use those in our gernal method.

# eg:
# class Mobile: #(object is optional !!)
#     def __init__(self,m):
#         self.model=m
#     def.show_model(self,p):
#         price=p #here it is local variable
        #we can wirte it like this also--->
        # self.price=p
        # print("Model : ",self.model,"price: ",price)


#------------------------Object:-------------------------

#object is class type variable or class instance . to use a class , we should create an object to the class.

#like when we write a=10 , here a is of type int. , same here object is class type variable. but that class and object , we make manually.

#so to use the class we have to create an object for it. otherwise we can not use that class.

#instance/object creation represent allotting memory necessary to store the actual data of the variables. means when we create methods and attribute in class , that time memory allocation does not happen. it happens when we create object for it(class).

#each time you create an object of a class of each variables defined in the class is created. in other words you can say that each object of a class has its own copy of data members defined in the class.

#creating object:
#syntax:
#object_name=class_name()

#if our method in our class has parameter , we can pass argument to those parameter , when creating class.

#object_name=class_name(arg)

#eg:
# class Mobile(object):
#     def __init__(self):
#         self.model="realme x"
#     def show_model(self):
#         print("Model : ",self.model)

# realme=Mobile()
#here realme is object for my class Mobile

#another eg:

# class Mobile_1(object): #writing(object) is nor neccessary
#     def __init__(self,m):
#         self.model=m
#     def show_model(self):
#         print("Model :", self.model)
# realme_1=Mobile_1("REALME X")


#-----------------how it works------------------------

# when i write realme=mobile(), a block of memory is allocated on heap. The size of allocated memory is to be decided from the attributes and method avialable in the class(Mobile).

#after allocating memory block, the special method __init__() is called internally. This method stores the initial data into the variables.

#the allocated memory location address of the instance is returned into object(realme)

#the memory location is passed to self.


#------------accessing class member using object---------- 

# we can access variable and mehtod of a class using class object or instance of class.
#object_name.variable_name.
#for eg:
#realme.model

# we can also access method like this:
#object_name.method_name()
# --or--
#object_name.method_name(argument)
# eg:
#realme.show_model()

#---------------------self-------------------------

#self is a default variable that contains the memory address of the curruent object.

#a class can have as many object , but self only contains memory address of the current object.

#this variable is used to refer all the instance variable and method.

#when we create object of a class , the object name contains the memory location of the object.

#this memory location is internally passed to self, as self know the memory address of the object so , we can acess variable and method of object. **

#self is the first argument to any object method because the first argument is always the object refrence.


#each time you create an object of a class , a copy of each variable , attribute and mehtod defined in the class is created for all of its objects.means for each object of class will have different memory location, and changes in one object does not affect the other object of same class.



#EXAMPLE 1:

class My_class(object):
    #if i do not want instance variable , so , i have not weitten it.
    def show(self):
        print("i am method")
x=My_class() #creation of object
x.show() #calling of object

#Example 2:
class Mobile:
    def __init__(self):
        self.model="RealMe z"
    def show_model(self):
        print("Model:", self.model)
    
realme=Mobile() #creation of object
realme.show_model() #calling of objects.
print(realme.model) #accessing the instance variable.
realme.model="realme pro" #updating instance variable.
print(realme.model) #accessing instance variable.

#EXAMPLE 3

class Laptop(object):
    def __init__(self,m):
        self.model=m
    def show_me(self,p):
        price=p #here we can also write self.price=p
        print("model: ",self.model,", price: ",price)

asus=Laptop("ROG") #this argument is for m parameter in __init__ method.
asus.show_me(300000) #this argument id for p parameter in show_me  method.
# ------------------chechking memory address------
print(id(asus))
dell=Laptop("dell xps")
dell.show_me(100000)
print(id(dell))

#the different memory allocation is given for different object, not depend on the value we pass to that object.
# like in noramal variable creation if two variable have same value will have same memory location and tagging different name, but in opp case there is different memory allocation is provided for each object of a class.
