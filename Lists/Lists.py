"""
Lists are a collection of data
"""


my_list = [80, 96, 72, 100, 8]
print(my_list)
my_list.append(1000)
print(my_list)
my_list.insert(2, 1000)
print(my_list)
my_list.remove(8)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.sort()
print(my_list)




'''
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
'''


zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]
zoo.pop(3)
zoo.append("Lizard")
zoo.pop(0)
print(zoo)
for x in zoo:
    print(x)
print(zoo[0:3])
i = 0
while i < 3:
    print(zoo[i])
    i += 1