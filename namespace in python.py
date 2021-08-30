#before namespace letk's understand what is name, name is simply a name given to object.Everything in python is an object.name is a way to access the underlying an object.python itself keep all names in form of dictionary , where keys are the names and the values are the objects that the name is pointing toward.

#for eg:a=a , here 2 is an object stored in memory and a is the name associated it with. lets look how to use it.

a=2
print("id(2) = ",id(2))
print("id(a) = ",id(a))
#we have got the same id !!

#funciton are objects too, so a name can refer to them as well.
def printhello():
    print("hello")
a=printhello #here a , the name is also pointing towards what printhello is point to , and printhello is just a name. 
a()

# Now that we understand what names are, we can move on to the concept of namespaces.

# To simply put it, a namespace is a collection of names.
# In Python,you can imagine a namespace as a mapping of every name you have defined to corresponding objects.it is a memory block where names are mapped to objects.

#different namespace can coexist at a time.

#1. class namespace- a class maintains it's own namespace known as class namespace. In the class namespace , the nams are mapped to class variables.
#2. instance namespace -  every instance have it's own namespace known as instance namespace . in the instance namespace , the names are mapped to instance variable.


# for eg:
class mobile:
    fp=10
    red="yes"

realme=mobile()
redmi=mobile()

#here class namespace is the memory block, where collection of names(fp, red)  are mapping towards the objects(10,"yes"), this is classnamespace(fp--->10,red--->"yes")

#since fp and red are class variable , the objects of the class (realme,redmi) are also pointing toward the same object(10,"yes") , but here the collection of object names are pointing towards the vlaue(10,"yes") , then here this collection is called instance namespace (ralme-->10,redmi-->"yes").

#now since object is also pointing toward the same namespace we can access it from object as well as classname also
# eg:
print()
print(mobile.fp)
print(realme.fp)

#if we change the class variable using the class name , then it will change for all objects. but if we change the class variable , using the class object then it will change for that specific object.
# eg:
print()
realme.fp=100
print(realme.fp)
print(mobile.fp)