#Basic Creation:
# Create a tuple with 5 student names.
mytuple = ( "Ashas", "Musab", "Irha", "Aima", "Ali" )
print(mytuple)
#Accessing Elements: Extract the third student's name from the tuple.
mytuple = ( "Ashas", "Musab", "Irha", "Aima", "Ali" )
print(mytuple[2])
#Indexing: Find the index of a student's name in the tuple
print(mytuple.index('Ali'))
#Tuple to List: Convert a tuple into a list.
my_list = list(mytuple)
print(my_list)
#List to Tuple: Convert a list into a tuple.
my_tuple = tuple(my_list)
print(my_tuple)
# Example list
my_list = [1, 2, 3, 4, 5]
# Convert the list to a tuple
my_tuple = tuple(my_list)
# Print the resulting tuple
print(my_tuple)

#Tuple Unpacking: Given a tuple (x, y, z), unpack its values into three variables.
# examle tuple
my_tuple = (2,4,6)
# unpack tuple
x,y,z = my_tuple
print(x)
print(y)
print(z)


