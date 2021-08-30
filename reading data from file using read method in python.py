#reading data from file :-

#read(size) : This method is used to read data/content from a file and returns it as string in text mode or bytes object in binary mode. 

# syntax : file_object.read(size)
#where size represent the number of bytes to be read from the begining of the file.
#when size is omitted or negative, the entire contents of the file will be read and returned.
#if the end of the file has been reached , file_object.read() will return an empty string('').


f=open('anything1.txt',mode='r')
data=f.read()
print(data)
f.close()
print("comleted !!!")
