#                                                  *Args
# parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
#    args[0] = 0 ## TypeError: 'tuple' object does not support item assignment
    args = list(args) ## list support item assignment
    args[0] = 100
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))

#                                                   **Kwargs
# parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    print("Hello "+ kwargs['first'] + " " + kwargs['last'])

hello(first="Oskar",middle="Arkadiusz",last="Paw")

def hell(**kwargs):
   print("Hello")
   for key,value in kwargs.items():
       print(value)

hell(first="Oskar",middle="Arkadiusz",last="Paw")

def hel(**kwargs):
   print("Hello",end=" ")
   for key,value in kwargs.items():
       print(value,end=" ")

hel(title="Mr.",first="Oskar",middle="Arkadiusz",last="Paw")




