#Thread class of threading module is used to creat threads.TO create our own thread we need to create an object of Thread Class.

#Following are the ways of creating threads:
#creating a thread without using a class
#creating a thread by creating a child class to Thread class
#creating a thread without creating child class to thread class.

#----------------------------------------------------------
#creating a thread w/o creating a child class to Thread class.


#we can create an independent thread child class that does not inherit from Thread Class from threading module.

#class ClassName(object):
    # statements
#object_name=ClassName()
#thread_object=Thread(object_name.function_name,args=())
#thread.start()

from threading import Thread
class Hello(object):
    def __init__(self):
        pass
    def friend(self,f_no):
        print(f"i have {f_no} number of friend !!")
o=Hello()
t=Thread(target=o.friend,args=(10,))
t.start()
