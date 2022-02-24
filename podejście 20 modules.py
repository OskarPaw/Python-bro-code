#                                                       Module
# a file containing python code
# may contain functions,classes, etc
# used with modular programming, which is to separate a program into parts
# help("modules") get us all modules

# created other file names messages with modules made below
# def hello():
#     print("Hello")
#
# def bye():
#     print("Bye")

# we can import modules made by us in other file 
import messages as msg # messages created in other python file

msg.bye() # function created in other file
msg.hello()

# other way of doing it
from messages import hello,bye

hello()
bye()

# importing everything from our made module/file, if they file is a big one it's risky to use it due to poss naming conflict
from messages import *

hello()
bye()