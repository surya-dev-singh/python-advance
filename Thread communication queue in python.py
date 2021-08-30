#The queue class of queue module is useful to create a queue that holds the data produced by the producer.
#the data can be taken from the queue and utilized by the consumer.

#we need not use locks since queues are thread safe.

#creating queue object:

# from queue import Queue
# q=Queue()

#Queue mthods:

#1. put() - this method is used by producer to insert item into the queue.
#syntax : queue_object.put(item)
# eg: q.put(i)

#2. get() - This method is used by consumer to retrieve items from the queue. 
#syntax:- producer_object.queuue_object.get(item)
# eg:- p.q.get(i)
 
#3. empty() - This mehtod returns True if queue is Empty else returns False.
#eg: q.empty()

#4. full() - This method returns True if queue is full else returns False.

from threading import Thread
from queue import Queue
from time import sleep

class Producer:
    def __init__(self):
        self.q=Queue()
    def produce(self):
        for i in range(1,6):
            print("Item produced...",i)
            self.q.put(i)
            sleep(1)
class consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        for i in range(1,6):
            print("Item recived",self.prod.q.get(i))
p=Producer()
c=consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()

# from threading import Thread
# from queue import Queue
# from time import sleep
# q=Queue()
# def test1():
#     for i in range(1,5):
#         print("hello friend... ",i)
#         q.put(i)
#         sleep(1)
# def test2():
#     for i in range(1,5):
#         print("bye friend....",q.get())
# t1=Thread(target=test1)
# t2=Thread(target=test2)
# t1.start()
# t2.start()
