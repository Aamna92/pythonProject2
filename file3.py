# Let's first create a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# this my_list will be a global variable that will be called into the function


# taking my_list and index as an argument in func_index function
def func_index(my_list, index):
    # if instane is not present then...
    if not isinstance(index, int):
        return "Invalid input: Index must be an integer."  # returning this output

    try:
        element = my_list[index]
        return element

    except IndexError:
        return "Error message: Index is out of range."  # if index is out of range then return this output


# Let's take an index
index = ["a"]
result = func_index(my_list, index)
print(result)  # Output would the specified index or error message or invalid input
