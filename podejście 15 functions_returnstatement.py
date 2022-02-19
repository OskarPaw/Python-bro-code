#                                                       Functions
# function = a block of code which is executed only when it is called
def hello(name):
    print("hello! " +name)
    print("second line")

hello("Oskar")
hello("Hans")

my_name = ("Arek")
hello(my_name)

# matching amount of arguments and parameters is a must
try:
    def hell(nam):
        print("hello "+ nam)
        hello("Oskar", "Paw")
except Exception as e:
    print(e)
print("The amount of arguments have to match the amount parameters")

def hel(first_name,last_name,age): # parameters
    print("hello "+first_name+" "+last_name)
    print("You're "+str(age)+" years old")

hel("Oskar","Paw",21) # arguments

#                                              Return Statements
# functions send python values/objects back to the caller
# these values/objects are known as the function's return value

def multiply(number1,number2):
    result = number1 * number2
    return result    # it sends back outcome to the  caller

# shorter way of making the same function
#def multiply(number1,number2):
    #return number1 * number2

# there are 2 ways of getting our function out of caller
print(multiply(5,5))  #first way

x = multiply(5,5)     #second way
print(x)
