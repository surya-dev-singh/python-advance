from threading import Thread
class Mythread(Thread):
    def __init__(self,a):
        print("child thread constructor !!")
        super().__init__() #here we need to call the constructor of parent class
        # beacuse since child class constructor overrids the parent class constructor , ans if parent class constructor is override then run method will not perform what it was meant for (perform a task when thread is started). so while initializing things for our child class using constructor , we need to intialize the constructor of parent class so that , run method can perform the given task!!.

        #but if we do not write the the constructor in our child thread class then the constructor of Thread class is inherited automatically and the run function is overide the one written in original Thread class(the method with same name overrides !!)

        #we can also call the Thread class constructor like this:
        # Thread.__init__()
        self.a=a
    def run(self):
        print(self.a)
t=Mythread("zero")
t.start()