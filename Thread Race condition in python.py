from threading import Thread, current_thread
class Flight:
    def __init__(self,available_seat):
        self.available_seat=available_seat
    
    def reserve(self, need_seat):
        print("Available seats :",self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().getName()
            print(f"{need_seat} seat is alloted for {name}")
            self.available_seat -= need_seat
        else:
            print("sorry !! All seats has alloted ")
f=Flight(1)
t1=Thread(target=f.reserve,args=(1,), name="rahul")
t2=Thread(target=f.reserve,args=(1,),name="sonam")
t1.start()
t2.start()



#race condition is a situation that occurs when threads are acting in an unexpected sequence, thus leading to unreliable output.
#this occurs when an program is using multithreading and more than one thread work at same time(there default nature) which generate unreliable output this is called race condition.
#this can be eliminated using thread synchronization.
