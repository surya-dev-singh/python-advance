# with statement :

#The with statement can be used while opening a file.
#when we open a file using with statement there is no need to close the file explicitly.

with open("lastone.txt") as f:
    data=f.read()
    print(data)
    print(f.closed)

print(f.closed)