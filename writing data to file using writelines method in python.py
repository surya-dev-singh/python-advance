#write() : This method is used to store/write character or string into the file represented by the file objecct. It returns the number of character written .
# syntax : file_object.write(string)

#writelines(): This method is used to store/write group of strings(list, tuple,set ) into the file represented by the file object.
#syntax : file_object.writelines(group of strings)

f=open("new.txt","w")
lst=['rahul','sonam','sumit','rani','raj']
# lst=["rahul\n","surya\n","raj\n"]
f.writelines(lst)
f.close()
print("success")