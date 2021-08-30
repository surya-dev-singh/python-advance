#if we want to use a fil e or its data, first we have to open it.
#open() - open() function is used to open a file. it return a pointer to the beginning of the file.This is called file handler or file object.

#syntax:  open("filename" , mode="r", buffering , encoding=None , errors=None, newline=None, closefd=True, opner=None)

# *filename- it represent a name of file
# *mode - it represent thre purpose of opening the file . It defaults to 'r' which means open for reading in text mode.
# *buffering - it is an iteger value used to set the size of the buffer for the file. In the binary mode we can pass 0 as buffering integer to inform not to use any buffering . In text mode we can pass 1 for buffering to reterieve data from the file one line at a time. we can pass any positive integer. Default is 4096 or 8192 bytes.
# *encoding - name of the encoding used to decode or encode the file. it should be used only in text mode . eg: utf-8
# *errors - an optional strings that specifies how encoding and decoding error are to be handled , this cannot be used in binary mode. Some of the standard values are strict , ignore,replace etc. 
# *newline - this parameter controls how universal newlines mode works(it only applies to text mode) it can be None, " ,'\n' , 'r','\r\n'.
# closedfd - if closedfd is False and a file descripter rather than a filename was given ,the underlying file descripter will be kept open when the file is closed. if a filename is given closefd must be True(the deafault) otherwise an error will be raised.
# *opener - A custom opener can be used by passing a callable as opener.



f=open("student.txt" ,"w")
 
#here f is file handler/file object 
#we can also give full path of file 
#default file opening mode is 'r'


