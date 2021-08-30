# r+ (read the write)

# f=open("root.txt","r+")
# data=f.read()
# f.write("\nhello robot")
# print(data)
# f.close()

#w+ (writing and then reading)
print("####################################")
# f=open("root2.txt","w+")
# f.write("youtube")
# #now the cursor is at the last , to you first have to seek it to 0
# f.seek(0)
# data=f.read()
# print(data)
# f.close()


#a+ (append and then read )
print("####################################")
f=open("root3.txt", mode="a+")
f.write("flag")
f.seek(0)
data=f.read()
print(data)
f.close()

