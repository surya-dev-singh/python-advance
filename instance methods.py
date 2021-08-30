#types of methods--->
#1. instance method :--
        # ---accessor methods
        # ---mutator methods
#2. class methods 
#3. static methods

#in variable concept of oop, class and static variable were same, but in case of methods in oops, static and class are different methods types.


#--------------instance methods---------------------
#instance methods are the methods which act upon the instance variables of the class.
#instance mehtod need to know the memory address of the instance which is provided through self variable by deafault ad first parameter for the instance method.

#syntax:-
# def method_name(self):
    # function 

#Instance method w/o parameter
class Mobile:
    def __init__(self):
        self.model="Realme X" #instance variable
    #instance mthod
    def show_model(self):
        print("MODEL: ",self.model)
realme=Mobile()
realme.show_model()

#Instance method with parameter
class Name:
    def __init__(self):
        self.name="surya "
    def my_name(self,surname):
        print(self.name+surname)
my_name=Name()
my_name.my_name("dev")
 