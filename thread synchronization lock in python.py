 # from threading import Thread, current_thread
# class Flight(object):
#     def __init__(self,available_seat):
#         self.available_seat=available_seat
#     def reserver(self,need_seat):
#         print("available seat :",self.available_seat)
#         if(self.available_seat>=need_seat):
#             name=current_thread().name
#             print(f"{need_seat} is alloted for {name}")
#             self.available_seat-=need_seat
#         else:
#             print("sorry !! all seats has alloted")

# f=Flight(1)
# t1=Thread(target=f.reserver,args=(1,))
# t1.setName="rahul"
# t2=Thread(target=f.reserver,args=(1,))
# t2.setName="sonam"
# t1.start()
# t2.start()

#----------------------------------------------------------

#many thread trying to access the same object lead to problem like making data inconsistent or getting unexpected output So when a thread is already accessing an object, preventing any other thread acessing the same object is called Thread Synchronization.

#The object on which the thread are synchronized is called synchronized object or mutually exclusive lock(mutex).

#thread synchronization is recommended when multiple thread are acting on the same object simultaneously and we want to prevent thread race.

#There are following techniques to do Thread synchronization:

#using Lock
#using RLock(Re-Entrant Lock)
#using semaphores

#----------------------------------------------------------

#Lock:-

#locks are typically used to synchronize access to a shared resource .Lock can be used to lock the object in which the thread is acting.A Lock has only two states, locked and unlocked .It is created in the unlocked state.

#in lock we need to learn two method.
#acquire()
#relese()

#acquire():
#This method is used to changes the state to locked and return immediately.When the state is locked , aquire() blocks until a call to release() in another thread changes it to unlocked, then the aquire() call reset it to locked and returns.
#syntax:- acquire(blocking=True,timeout=-1)
    #true:- it blocks until the lock is unlocked, then set it to locked and return True.
    #false:- it does not block .if a call with blocking set to True would block, return False immediately; otherwise , set the lock to locked and return True. 
    #timeout:- when invoked with the floating-point timeout argument set to a positive value, black for at most the number of seconds specified by timeout and as long as the lock cannot be acquired .A timeout argument of -1 specifies an unbounded wait.It forbidden to specify a timeout when blocking is false.




# relese ():
# This method is used to relese a lock .This can be called from any thread, not only the thread which has acquired the lock.

# when the lock is locked , reset it to unlocked, and return . If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.

# when invoked on an unlocked lock, a RuntimeError is raised.

# there is no return value
#syntax: relase()

#----------------------------------------------------------

from threading import Thread, current_thread, Lock
class Flight(object):
    def __init__(self,available_seat):
        self.available_seat=available_seat
        self.l=Lock()
    def reserver(self,need_seat):
        self.l.acquire(blocking=True,timeout=-1) #this are default parameter , we do not need to write this parameter.
        print("available seat :",self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f"{need_seat} is alloted for {name}")
            self.available_seat-=need_seat
        else:
            print("sorry !! all seats has alloted")
        self.l.release()

f=Flight(2)
t1=Thread(target=f.reserver,args=(1,),name="rahul")
t2=Thread(target=f.reserver,args=(1,),name="sonam")
t3=Thread(target=f.reserver,args=(1,),name="raj")
t1.start()
t2.start()
t3.start()

#now if i also make one main thread like this : 
# print("main thread !!")
#then this will intrupt the execution of other thread (means the result of main thread will shown while result of upper three threads are showing) , now in order to fix it , we can use join() on t1 , t2, t3 . so that other thread (including main thread runs after the execution of upper three thread.)