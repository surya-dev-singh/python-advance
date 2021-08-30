#multitasking using multiple thread :
#when multiple task are executed at a time , then it is called multi-tasking.For this purpose we need more than one thread and when we use more than one thread , it is called multi-threading.

#now we will look for two task using two thread

from threading import Thread
class Hotel(object):
    def __init__(self,t):
        self.t=t
    def food(self):
        for i in range(1,5):
            print(self.t,i)
        
h1=Hotel('take order from table')
h2=Hotel("serve order to table")
t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
# t1.join()
t2.start()



#so above is example of multitaskig with multiple thread !!