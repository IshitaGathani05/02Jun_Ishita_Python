# Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    file = open("sample.txt", "r")
    
    # Try to read the content
    content = file.read()
    print("File content:\n", content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except IOError:
    print("Error: An I/O error occurred while accessing the file.")

finally:
    # Ensure the file is closed if it was successfully opened
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")
