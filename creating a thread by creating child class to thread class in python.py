#creating a thread :
#thread class of threading module is used to creat threads. To create our own thread we need to create an object of Thread class.
#following are the ways of creating threads:
#creating a thread without using a class
#creating thread by creating a child class to Thread class.


#----------------------------------------------------------
#creating a thread by creating a child classs to thread class :

#we can create own thread child class by inheriting Thread class from threading module.
# eg:
# class Childclassname(Thread):
#     statmets
# thread_object=Childclassname()

# from threading import Thread
# class Mythread(Thread):
#     pass
# t=Mythread()
# print(t.name)

#----------------------------------------------------------

#thread class's methods:

#1.start(): once a thread is created it should be started by calling start() method

#2.run(): every thread will run this method when thread is started .we can ovveride this method and write our own code as body of the method .A thread will terminate automatically when it comes out of run() method.

#3.join(): this method is used to wait till the thread completely executes the run() method.

#----------------------------------------------------------

from threading import Thread
class mythread(Thread):
    def run(self): #this run method is already in Thread class but we are writing it again(means overriding it in our child class)
        print("Run method")
        print("----------------------------")
        for i in range(5): # this task is executed by child thread
            print("child thread")
t=mythread()
print(t.name)
#now since run() will call only when thread is started to lets start the thread.
t.start()
#now since there is two task running independently by two different thread so , out put of two task wiil be random ,
#now if i want that firt let the task of child class run and then the task of other class should run, to do this we have join() method in our Thread class from ehich our child class has been derived . eg:
t.join()
#now first out put of child thread will be displayed then the output of main class is displayed.
for i in range(5): #this task it executed by main thread 
    print("main thread"  )
