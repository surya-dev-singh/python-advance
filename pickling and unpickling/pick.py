import pickle,stu
#pickling storing object in the file .
n=int(input("enter the number of student :"))
with open("student.dat",mode="wb") as f:
    for i in range(n):
        name=input("enter student name : ")
        roll=int(input("enter student roll number : "))
        address=input("enter the address : ")
        stu1=stu.Student(name,roll,address)
        pickle.dump(stu1,f)

print("pickling done !!!")
