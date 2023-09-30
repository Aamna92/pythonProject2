# Create a set of colors
myset = {"red", "green", "blue"}
print(myset)
#Adding Elements: Add "yellow" to the set.
myset.add("yellow")
print(myset)
#Removing Elements: Remove "red" from the set.
myset.remove("red")
print(myset)
#Union: Find the union of two sets.
set1 = {"red", "yellow" , "blue"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Intersection: Find the common elements of two sets.
set1 = {"red", "yellow" , "blue"}
set2 = {"yellow","green","orange"}
set3 = set1.intersection(set2)
print(set3)
#Difference: Identify the difference between two sets.
x = {"red", "yellow" , "blue"}
y = {"yellow","green","orange"}
z = x.difference(y)
print(z)
#Subset Checking: Check if {"red", "green"} is a subset of {"red", "green", "blue"}.
set4 = {"red", "green"}
set5 = {"red", "green", "blue"}
set6 = set4.issubset(set5)
print(set6)

#Set to List: Convert a set into a list.
my_set = {"apple", "banana", "cherry"}
my_list = list(my_set)
print(my_list)

#List to Set: Convert a list into a set.
my_list = ['apple','banana','cherry']
my_set = set(my_list)
print(my_set)
#Set Comprehension: Create a set of numbers divisible by 3 from 1 to 15 using set comprehension.
divisible_by_3 = {x for x in range(1, 16) if x % 3 == 0}
print(divisible_by_3)

