# text mode - a file opened in text mode, treats its contents as if it  contains text strings of the str type.
#when you get data from a text mode file, python first decodes the raw bytes using either a platform-dependent econding or , specified one.

#binary mode - a file opened in binary mode, python uses the data in the file without any decoding, binary mode file reflects the raw data in the file.
 

f=open("student.txt", mode="w")
f.write("hello\n")
f.write("freind\n")
f.write("how are you")
f.close()
print("writing success")
#here in text mode
f=open("student.txt",mode="r")
data=f.read()
print(data)
f.close()

#here in binary mode python is not decoding while executing program
f=open("student.txt",mode="br")
data=f.read()
print(data)
f.close()

# in unix \n is refer to as new line , but in windows \r\n is refer to as new line.
