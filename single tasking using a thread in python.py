#Single Tasking Using a Thread :
# When multiple task are executed by a thread one by one, the it called single tasking. 
from time import sleep
from threading import Thread
class MyExam(object):
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()
        self.q4()
    def q1(self):
        print("question 1 solved")
        sleep(2)
    def q2(self):
        print("question 2 solved")
        sleep(2)
    def q3(self):
        print("question 3 solved")
        sleep(2)
    def q4(self):
        print("question 4 solved")
        sleep(2)

mye=MyExam()
t=Thread(target=mye.solve_question)
t.start()
#we can even specify sleep() in every question like sleep(2) 
