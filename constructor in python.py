#python support special type of method called constructor for initializing the instance variable of a class.

#A class constructor(__init__()), if defined is called whenever  a program creates an object of that class.

# A costructor is called only once at the time of creating an instance.

#if two instances are created for a class , the constuctor will be called once for each instance.

#since constuctor is called automatically , we can verify it like this--->
class Mobile(object):
    def __init__(self):
        print("Mobile constructor called !!")
realme=Mobile() #note here , we are just defining our object , we have not called any method.