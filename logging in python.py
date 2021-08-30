# logging  : 

# logging is usefull to track the error or exception or information . It also help debugging.

# we use logging module to log the error

# syntax
# import logging
# or 
# from logging import *

# ------------------------------------------------------------------------------
# basicConfig(**kwargs) method

# this method is used to config the logging system.
# syntax :
# basicConfig(**kwargs)

# filename-It specifies that a FileHandler be created, using the specific filename, rather than a StreamHandler.

#filemode - If filename is specified , open the file in the mode . Default to 'a'. We can write 'W'.

#level- set the root logger level to the specified level.       
#        
#format - use the specifed format string for the handler.  

#datefmt - use the specifed date/time format , as accepted by time.strftime()

#style - if format is specifed , use this style for the format string. one of '%' ,'{' or '$' for printf-style ,str.format() or string. Tempalte respectively . Defaults to '%'.

# there are other arguments also :
#stream
#handler 
#force


#------------------------------------------------------------------------------------

# level :

# NOTSET -------> 0
# DEBUG --------> 10
# INFO ---------> 20
# WARNING ------> 30
# ERROR --------> 40 
# CRITICAL ------> 50

# by default level is 30 , i.e warning 

#----------------------------------------------------------------------------------------

# methods 

# getLogger() - This method returns a logger with the specified name or , if name in None, reuturn a logger which is the root logger of the hierarchy . If specified , the name is typically a dot-seperated hirarchial name like 'a' , 'a.b' or 'a.b.c.d'

#info(msg) - This will log a message with level INFO on this logger.

#warning(msg) - This will log a message with level WARNING on this logger.

#error(msg) - This will log a message with level ERROR on this logger.

#critical(msg) - This will log a message with level CRITICAL on this logger.  

#exception(msg) - This will log a message with level ERROR on this logger.  


#-------------------------------------------------------------------------------------

#format 

# format can take a string with LogRecord attributes in any arrangement you like .   


#asctime -  Human-readable time when the LogRecord was created . By default this is of the form '2003-07-08 16:49:45,896' (the number after the comma are millisecond portion of time)  

# eg :  %(asctime)s   

# created - Time when the LogRecord was created (as returned by time.time()).

# eg: %(created)f 

# filename - Filename portion of pathname.    

#eg : %(filename)s

#levelname - Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')

#eg : %(levlevelname)s

#levelno - numeric logging level for the message ('DEBUG', 'INFO', 'WARNING','ERROR','CRITICAL')

#eg   %(levelno)s

#message - The logged message , computed as % arg .This is set when Formatter.format() is invoked .  
#eg %(message)s

# similarly we have lineno , name , pathname, ........... adn so on (check the official doc)

# ----------------------------------------------------------------------------------------

from logging import *

# now defalut level is 30 , i.e warnning   , now  we can display above warning (error and critical) , if i try to view debug and info , we wont be able to see it !!

# debug("this is debug") #this will show default log record.
# warning("this is warning") #this will show default log record.
# critical('this is critical') #this will show default log record.

# now above code will show output in console, but we have to log everyting in file, so in order to do that we have to use basicConfig()

basicConfig(filename='mylogfile.log', filemode='w', level=DEBUG,format='%(asctime)s /// %(message)s /// %(lineno)s /// %(name)s')
# now we are giving %()s style formatting , we can set different style using style attribute like style="{" and then we have to apply format in that style.
# now default name is root , we can change it by using getLogger() method
logger=getLogger("surya")
# now to get entry for this specific logger we have to use logger before every method .
# or else it will use root as default name 
logger.debug("this is debug")
info('this is info')
warning('this is warning')
error("this is error")
critical('this is critical') 





