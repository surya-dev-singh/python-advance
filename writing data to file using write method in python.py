#writing data to the file :-

#write() : This method is used to store/write character or strings into the file represented by the file object. It returns the number of character written.

#syntax : file_objec.write(string)

f=open("test.txt", mode='w')
n=f.write("hello friend")
f.write("test_1\n")
f.write("test_2")
print(n)
f.close()
