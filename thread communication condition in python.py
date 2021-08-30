#condition class is used to improve speed of communication between Threads.
#The condition class object is called condition variable.

#a conditon variable is always associated with some kind of lock; this can be passed in or one will be created by default . passing one in is useful when several condition variables must share the same lock.The lock is part of the condition object: you don't have to track it seperatly.
#a condition is a more advance version of the event object.


#create condition object
# from threading import Condition
# cv=Condition()


#condition method:

#1. notify(n=1) - This method is used to immedietely wake up one thread waiting on the condition .Where n is number of thread need to wake up.

#2. notify_all() - This method is used to wake up all threads waiting on the condition.

#3. wait(timeout=None): This method wait until notified or until a timeout occurs. if the calling thread has not acquired the lock when this method is called , a RuntimeError is raised. Wait terminates when invokes notify() method or notify_all() method. The return value is Tre unless a given timeout expired, in which case it is False.



from threading import Thread , Condition
from time import sleep
lst=[]
def produce():
    cv.acquire()
    for i in range(1,6):
        lst.append(i)
        sleep(1)
        print("item produced...")
    cv.notify()
    cv.release()
def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)
cv=Condition()
t1=Thread(target=produce)
t2=Thread(target=consume)
t1.start()
t2.start()
