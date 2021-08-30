class Student(object):
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address
    def disp(self):
        print(f"name : {self.name} roll : {self.roll} address : {self.address}")
        