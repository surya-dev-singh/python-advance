#when we start any python program, one thread begins running immeditely, which is called main thread of that program created by PVM.

#The main thread is created automatically when you program is started.

#now in order to see that main thread, we have to import threading module 

import threading
t=threading.current_thread().getName() #here current_thread(). is function !!.
print(t)

