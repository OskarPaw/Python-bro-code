#                                                       Dictionaries
# dictionary = A changeable, unordered collection of uniques key:value pairs
#               Fast due to hashing,allow us to acces a value quickly

capitals = {'USA':'Washinhton DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'USA':'Las Vegas'})
capitals.pop('China') #usuwa tylko wybrany element
#capitals.clear() usuwa wszystko

print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Germany':'Berlin'})

for key,value in capitals.items():
    print(key,value)

#                                                      Indexing
# index operator [] = gives access to a sequence’s element (str,list,tuples)

name = "Oskar Sql!"

# if(name[0].islower()):
# name = name.capitalize()

first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]
character_from_the_back =name[-2] # random character counting backwards

print(first_name)
print(last_name)
print(last_character)
print(character_from_the_back)