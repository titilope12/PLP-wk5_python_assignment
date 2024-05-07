# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with a mix of text and numbers: 9876\n")
except IOError as e:
    print("Error occurred while creating the file:", e)

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Content of my_file.txt:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("6789\n")
        file.write("Yet another appended line with a mix of text and numbers: 54321\n")
        print(file.read())
except IOError as e:
    print("Error occurred while appending to the file:", e)
except PermissionError:
    print("Permission denied.")
finally:
    print("File operations completed.")

'''with open("my_file.txt","r") as file:
    print(file.read())'''