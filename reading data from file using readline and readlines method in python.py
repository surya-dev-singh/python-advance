#reading data from file : -------------

#readline() : this method is used to read single line from a file.
#syntax : file_object.readline()

#readlines() : this method is used to read all lines from a file. it will retrun list of line.
#syntax : file_object.readlines()

f=open("anything2.txt","r")
data=f.readline()
data2=f.readline()
print(data)
print(data2) #here we are getiing two new beacuse one , we have in out file and other form print function.
f.close()

f1=open("anything3.txt","r")
data3=f1.readlines() #this will returns the list of lines
# print(data)
for i in data3:
    print(i)
f.close()
