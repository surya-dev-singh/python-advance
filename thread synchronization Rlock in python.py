#Rock :

#A reetrant lock is a synchronication primitive that may be acquired multiple times by the same thread.

#The standard lock doesn't know which tread is currently holding the lock .If the lock is held , any thread that attempts to acquire it will block , even if the same thread itself holding the lock. In such cases, Rlock(re-entrant lock) is used.

#a reentrant lock must be relese by the thread that acquired it. Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking ; the thread must relese it once for each time it has acquired it .

from threading import Thread, current_thread, RLock,Lock
class Flight(object):
    def __init__(self,available_seat):
        self.available_seat=available_seat
        self.l=RLock()
        # print(self.l)
    def reserve(self,need_Seat):
        self.l.acquire(blocking=True)
        self.l.acquire()
        # print(self.l)
        print(f"available seat :{self.available_seat}")
        if (self.available_seat>=need_Seat): 
            name=current_thread().getName()
            print(f"{need_Seat} has been alloted to {name}")
            self.available_seat-=need_Seat
        else:
            print("sorry !! no seat is left")
        self.l.release()
        self.l.release()
f=Flight(2)
t1=Thread(target=f.reserve,args=(1,),name="rahul")
t2=Thread(target=f.reserve,args=(1,),name="sonam")
t3=Thread(target=f.reserve,args=(1,),name="raj")
t1.start()
t2.start()
t3.start()