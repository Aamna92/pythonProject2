def reverse_file(filename):
    try:
        # Open the file in read mode to read its content
        with open(filename, 'r') as file:
            # Read the content of the file
            file_content = file.read()

        # Reverse the content
        #reverse the content by using Python's string slicing with [::-1]
        reversed_content = file_content[::-1]

        # Open the file in write mode to write the reversed content back
        with open(filename, 'w') as file:
            # Write the reversed content back to the file
            file.write(reversed_content)

        print(f"Content of '{filename}' has been reversed and saved back to the file.")
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")

# Example usage:
filename = 'example.txt'
reverse_file(filename)
#read lines
f= open("example.txt","r")
print(f.readlines())

