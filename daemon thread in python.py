# A daemon thread  is a thread which runs continuously in the background. 
# it provides support to non-daemon threads.

# when last non-daemon thread terminates, automatically all daemon threads will be terminated. we are not required to terminate daemon thread explicitly.

#create daemon thread:
# setDaemon(True) method or daemon=True properperty is used to make a thread a Daemon thread.

# eg:
# t1=Thread(traget=disp)
# t1.setDaemon(True)
# t1.daemon=True

#methods :

#1. setDaemon(True/False) - This method is used to set a thread as daemon thread. you can set thread as daemon only before starting that thread which means active thread status cannot be changed as daemon.
#if we pass True non-daemon thread will become daemon and if False daemon thread will become non-deamon.

#2. daemon property - This property is used to check whether a thread is daemon or not. It returns True if thread is daemon else False.we can also use daemon property to set a thread as daemon thread or vice-versa.

#3. isDaemon() - This method is used to check whether a thread is daemon or not . It returns True if thread is daemon else False.

# from threading import Thread
# def disp():
#     print("Daemon Threads")
# t1=Thread(target=disp) 
# print(t1.isDaemon())
# t1.setDaemon(True)
# print("------")
# print(t1.isDaemon())
# t1.start()
# print("------")
# print(t1.daemon)
#similarly we can set t1.daemon=true/false ,but not on active thread.
print("**************************************************")

#default nature of thread----

#Main Thread is always non-daemon thread
# from threading import current_thread
# print("hello")
# ----print(current_thread().isDaemon())----
# mt=current_thread()
# print(mt.getName())
# print(mt.daemon)


#rest of the threads inherits daemon nature from their parents.
#if parent thread is non-daemon then child thread will become non-daemon thread.
#if parent thread is daemon then child thread will also become daemon thread.
print("*****************************")
# from threading import Thread, current_thread
# def disp():
#     print("Disp Function")
#     t2=Thread(target=show)
#     print("T2:", t2.isDaemon())
#     t2.start()
# def show():
#     print("show function")

# mt=current_thread()
# print(mt.getName())
# print("MT:", mt.isDaemon())
# t1=Thread(target=disp)
# print("T1 before:", t1.isDaemon())
# t1.setDaemon(True)
# t1.start()
# t1.join()
# print("main thread")


#when last non=daemon thread terminates, automatically all daemon threads will be terminates. we are not required to terminate daemon thread explicitly.


from threading import Thread,current_thread
from time import sleep
def teacher():
    for i in range(1,11):
        print("Teaching Session",i)
        sleep(1)
    
t1=Thread(target=teacher)
t1.setDaemon(True)#
t1.start()
sleep(6)
print("exam finished", current_thread().name )


