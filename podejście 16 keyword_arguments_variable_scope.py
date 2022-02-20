#                                                     Keyword Arguments
# arguments preceded by an identifier when we pass them to a function
# the order of the arguments doesn't matter, unlike positional arguments
# python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("hello "+first+" "+middle+" "+last)


hello(first="Oskar", last="Paw", middle="Arkadiusz")  # order got changed by first, middle, last

#                                                     Nested function calls
# function calls inside other function calls
# innermost(najgłębsza) function calls are resolved first
# returned value is used as argument for the next outer function

num = input("Enter a random number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input("Enter a random number: ")))))  # less space used way

#                                                     Variable scope
# the region that a variable is recognized
# a variable is only available from the inside the region it is created
# a global and locally scoped versions of a variable can be created

name = "Hans"  # global scope (available inside & outside functions)


def display_name():  # local scope ( available only inside this function)
    name = "Oskar"
    nam = "Arkadiusz"
    print(name)
    print(nam)


display_name()
print(name)
