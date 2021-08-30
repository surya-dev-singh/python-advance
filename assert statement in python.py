#assert statement :
# The assert statement is usefull to ensure that a given condition is true. if it is not true, it raise AssertionError.
# syntax : assert condition, error_mssage

#if the condition is False then the exception by the name AssertionError is raised along with the message.
#if message is not given and the codition is False then also AssertionError is raised without message.

a=20
assert a<=10 , "invalid number"

