#This is one of the oldest synchronization primitives in the history of computer science, invented by the early dutch computer scientist edsger w.dijkstra.

#a semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call.
#the counter can never go below zero ; when acquire() finds that it is zero , it blocks , waiting until some other thread calls release().

from threading import *
class Flight:
    def __init__(self,available_seat):
        self.available_seat=available_seat
        self.l=Semaphore(2)
        print(self.l)
    def reserve(self,need_seat):
        self.l.acquire()
        print("available seats : ", self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat-=need_seat
        else:
            print("sorry ! all seats has been alloted ")
        self.l.release()
        # self.l.release() we can call release as many number of time. but it would create sometime bug , so use bounded semaphores.
        #in bounded semaphore as many number of time we have use acquire method , we have to use realse method.
f=Flight(4)
t1=Thread(target=f.reserve, args=(1,),name="rahul")
t2=Thread(target=f.reserve,args=(1,),name="surya")
t3=Thread(target=f.reserve,args=(1,),name="test")
t1.start()
t2.start()
t3.start()

#do remember that sometimes in thread synchronization there occurs critical problem of dead lock.
