#Create a dictionary to store a book's title, author, and publication year.

thisdict = {
  "Book": " King Lear,",
  "Autor": "William Shakespeare",
  "year": 1608
}
print(thisdict)
#Accessing Elements: Extract the author's name from the dictionary.
thisdict = {
  "Book": " King Lear,",
  "Autor": "William Shakespeare",
  "year": 1608
}
print(thisdict["Auther"])

# Updating: Update the publication year to 2022.
thisdict = {
  "Book": " King Lear,",
  "Autor": "William Shakespeare",
  "year": 1608,
  "year": 2022
}
print(thisdict)
#Adding Elements: Add a list of chapters to the book dictionary.
thisdict['chapters'] = ['Chapter 1', 'Chapter 2', 'Chapter 3']
print(thisdict)
# Remove the publication year from the dictionary.
del thisdict["year"]
print(thisdict)
#Loop through the dictionary and print all the keys.
print("keys")
for key in thisdict:
  print(key)
#Looping through Value
print("values")
for value in thisdict.values ():
  print(value)
# Create a dictionary with numbers (1 to 5) as keys and their squares as values.
squares_dict = {num: num**2 for num in range(1, 6)}
print(squares_dict)
#Merge two dictionaries into one.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
