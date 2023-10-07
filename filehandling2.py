def read_and_print_file_content(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read and print the content of the file
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if 'file' in locals():
            file.close()

# Example usage:
filename = 'example.txt'
read_and_print_file_content(filename)
