#                                                                String format
# optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {} ".format("cow","moon")) # it also works with numbers
print("The {} jumped over the {} ".format(animal,item)) # it also works with numbers

# positional argument
print("The {1} jumped over the {0} ".format(animal,item))
print("The {1} jumped over the {1} ".format(animal,item))

#keyword argument
print("The {animal} jumped over the {animal} ".format(animal="cow",item="moom"))

# getting output by format string
text = "The {} jumped over the {}"
print(text.format(animal,item))

# adding space
name = "Oskar"

print("Hello, my name is {}. Nice to meet you".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # left aligned
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # right aligned
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # center

# formating numbers

number = 3.14159
number2 = 100000000000

print("The number pi is {:.2f}".format(number)) # f for floating point numbers with decimal portion
print("The number is {:,}".format(number2)) # , - adding commas automatically to all 1000s
print("The number is {:b}".format(number2)) # b - a binary representation of number
print("The number is {:x}".format(number2)) # X - in a hexadecimal
print("The number is {:X}".format(number2))
print("The number is {:o}".format(number2)) # o - in a octal number

#                                                               Random numbers
import random

# generating a random number between (x,y)
x = random.randint(1,6)

print(x)

# generating a random float number from 0:1
y = random.random()

print(y)

# making random choices from list
myList = ["rock","paper","scissors"]
z = random.choice(myList)

print(z)

# a shuffle method will shuffle a list or other collection
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards)

