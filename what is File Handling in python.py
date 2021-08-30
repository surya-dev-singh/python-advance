#files:
# file is the collection of data that is available to a program . we can retrive and use data stored in a file whenever we required.

#advantages :-

#stored data is permanent unless someone remove it .
#stored data can be shared.
#it is possible to update or remove the data.


#types of fles:

#there are two types of files:-
#1. text file - it strores data in the form of characters. It is used to store characters and strings.

#2. binary file - it stores data in the form of bytes , a group of 8 bits each. It is used to store text, images, pdf, csv, video and audio.


#dont worry at below code just, give it a look to understand what is file handling.

f=open("student.txt", mode="w")
f.write("hello how are you")
f.close()