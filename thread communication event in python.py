#what is thread communication ?

#when two or more threads communicate with each other is called thread event.

#there are three way for thread communication:

#1.event
#2.condition
#3.queue


#event: 

#this is one of the simplest mechanisms for communication between threads:
# one thread signals an event and other threads wait for it.

#an event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method. The wait() method blocks until the flag is true.

#The flag is initially false.


#----create event object----------:

#from threading import Event
#e=Event()  #here e is event object of event() class.


#----event methods----------:

#set(): It sets internal flag to true.All therads waiting for it to become true are awakened. Threads that call wait() once the flag is true will not block at all. 
 
#clear(): It reset the internal flag to false. subsequently , therads calling wait() will block until set() is called to set the internal flag to true again.

#is_set(): it return true if and only if the internal flag is true.

#wait(timeout=None): It blocks until the internal flag is true. if the internal flag is true on entry , return immediately. Otherwise, block until another thread calls set() to set the flag to true, or until the optional timeout occurs.
#when the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds(or fractions thereof). 
#This method returns true if and only if the internal flag has been set to true, either before the wait call or after the wait starts, so it will always return true except if a timeout is given and the operation timeout.


#eg:



from threading import Event,Thread
from time import sleep
def light_switch():
    sleep(3)
    e.set()
    print("green light ON")
    sleep(5)
    print("red light ON")
    e.clear()

def traffic():
    e.wait()
    while e.is_set():
        print("you can go.......")
        sleep(.5)
    print("program done")
e=Event()
t1=Thread(target=light_switch)
t2=Thread(target=traffic)
t1.start()
t2.start()

#eg2:

# from threading import Thread,Event
# from time import sleep
# def test1():
#     print("hello friend")
#     sleep(1)
#     e.set()
#     sleep(4)
#     print("bye friend")
#     e.clear()
# def test2():
#     e.wait()
#     if e.is_set()==True:
#         print("my name is surya")
#         print("i am not robot")
#     else:
#         print("...")

# e=Event()
# t1=Thread(target=test1)
# t2=Thread(target=test2)
# t1.start()
# t2.start()