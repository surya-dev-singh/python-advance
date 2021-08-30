# text file modes :--

# r : open for reading. the file pointer is positioned at the beginning of the file. if the file does'nt exist it will show filenotfounderror.

#w : open for writing . if any data is already present in the file , it will overwrite the data . if the file doesn't exist it will create that file.

#x : open for exclusive creation with write. The specified file must not be available, if the specified file is available it will show error FILEEXITERROR.

#a :  open for appending .The file pointer is positioned at the end of the file . it appends new data at the end of file. If the file does not exists it will create a new file for writing data.

#r+ : open for reading and then writing.

#w+ : open for writing and then reading. it will overwrite existing data. 

#a+ : open for appending then reading . it won't overwrite existing data.




#--all modes are same for binary file all we have to do is to write b after the mode--. eg: -

#rb
#wb
#xb
#ab
#rb+
#wb+
#ab+