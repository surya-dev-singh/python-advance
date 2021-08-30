#creating a thread :

#Thread class of threading module is used to create threads. To create our own thread we need to create an object of Thread class.

#following are the ways of creating threads:-
# 1 .creating a thread without using a your own class.
# 2. creating a thread by creating a child class to Thread class.
# 3. creating a thread without creating child class to Thread class.

#----------------------------------------------------------
# creating a thread without using your own class:

#this means that we do not need to create our own class. but we need to use Thread class from thread module.

# from threading import Thread
# thread_object=Thread(target=function_name,args=(arg1,arg2,.....))

# thread_object : it represent our thread
# target - It represent the function(or task) on which the thread will act .
#args : it represent a tuple of arguments which are passed to the function(or our task).
# eg:
# from threading import Thread
# t=Thread(target=disp,args=(10,20))

#----------------------------------------------------------

#now how to start a Thread:
#once a thread is created it should be started by calling start() method on our thread.
# from threading import Thread
# def disp(a,b):
#     print("Thread Running :",a,b)
# t=Thread(target=disp,args=(10,20))
# t.start()

#we can use it thead multiple times by using for loop:
# from threading import Thread
# def disp(a,b):
#     print("Thead running ",a,b)
# for i in range(5):
#     t=Thread(target=disp,args=(10,20))
#     t.start()

#----------------------------------------------------------------------

#now sice main thread is always running , then we and when we create and start our own thread by creating thred_object of Thread class , then we are having two thread running , one Main thread and Thread-1(the thread we defined using Thread class)

#now look at the below code , when we have two thread running then the output of both will show to console:
from threading import Thread
import threading
#now this is task on Thread-1(our custom Thread!)
def disp(p,q):
    for i in range(p):
        print(f"Thread {q} running !! ")
        print(threading.current_thread().getName())
        q+=1
t=Thread(target=disp,args=(5,101))
t.start()
#now this is task of main thread 
for i in range(5):
    print("Main Thread running !!")
#The output of both programm runs at the same time , so we see the output little messed up ! but this is how it works, we have run two task a same time.
#the order of output is unpredectable.
