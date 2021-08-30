#every thread has its name , the default thread(main thread) which always runs when pvm is called .
# the thread which you defined using Thread class from threading module has its name (thread-1,thread-2.....)

# now you can find(get) what is the name of my thread or you have to give name to you thread(set)

#some method we will look at :

#current_thread() : this function returs current thread object .
#getName():every thread has a name by default , to get the name of thread we can use this method.
#setName(name): this method is used to set the name of thread
#name Property- this property is used to get or set name of the thread.
# ---------------------------------------------------------

from threading import Thread, current_thread

# def disp():
#     print("child Thread object ", current_thread())
# t=Thread(target=disp)
# t.start()
# print("main thread",current_thread())

# the output of current_thread function has name of current thread nad a started code ( a unique number for each thread in every execution)

# for setiing a custom thread name:
def disp(p,q):
    print("default child thread name :",current_thread().getName())
    current_thread().setName("root"+str(p)+str(q))
    print("new child thread name :",current_thread().getName())
t=Thread(target=disp,args=(10,20))
t.start()
print("default main thread name",current_thread().getName())
current_thread().setName("kali")
print("new main thread name :",current_thread().getName())

# now we can also get the name of current thread ruunig by using the name property.
print()
print("main name :", current_thread().name)

#similary we can set the name of thread using name property:
current_thread().name="surya"
print("new main name :", current_thread().name)
print()
print("child thread name",t.name)
t.name="root-toor"
print("new child name",t.name)



#----------------------------------------------------------
# best way to give name to your thread rather then all above discuss method  , you can write like this :
def hello():
    pass
t=Thread(target=hello,name="suryadev thread")
print(t.name)