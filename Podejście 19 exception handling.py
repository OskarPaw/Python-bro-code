#                                                        Exception handling
# events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")

# Few more examples
# 1
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I don't understand that")
        continue
    if age < 0:
        print("Error, age cannot be negative number")
        continue
    else:
        break

if age >= 18:
    print("You are able to vote")
else:
    print("You are not able to vote")

# 2
while True:
    name = input("Please provide me your name in caps: ")
    if not name.isupper():
        print("Error, name is not in all caps")
    else:
        break

# 3
while True:
    selection = input("select from A to D: ")
    if selection.upper() not in ["A", "B", "C", "D"]:
        print("Invalid Option")
        continue
    else:
        print("This is valid option")
        break
