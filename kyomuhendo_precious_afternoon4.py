# File handling
"""
Opening a File:
The open() function is used to open a file and returns a file object.
 It takes two parameters: the file name (along with the path, if necessary) and the mode
 'r': Read mode (default), opens a file for reading.
'w': Write mode, opens a file for writing. Creates a new file if it doesn't exist, or truncates the file if it does.
'a': Append mode, opens a file for appending. Data is added to the end of the file.
'x': Exclusive creation mode, opens a file for writing only if it doesn't already exist.
'b': Binary mode, for working with binary files.
't': Text mode (default), for working with text files
"""
#USING THE READ MODE
file = None  # Initialize the file variable

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    if file:
        file.close()

# OPENING THE FILE IN WRITE MODE
file = open("output.txt", "w")

file.write("Hello, World!\n")
file.write("This is some text written to the file.\n")
file.write("Writing in Python is easy!")
file.close()

#DELETING A FILE
import os

file_path = "delete.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file '{file_path}' has been deleted.")
else:
    print(f"The file '{file_path}' does not exist.")

#APPENDING DATA TO DATA IN THE FILE
file_path = "append.txt"

try:
    # Open the file in append mode
    file = open(file_path, "a")
    file.write("This content will be appended to the file.\n")
    file.close()
except FileNotFoundError:
    print("The file does not exist.")

#READING LINE BY LINE
file_path = "example.txt"

with open(file_path, "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character at the end of each line

# READ ONLY PARTS OF THE FILE
try:
    f = open("example.txt", "r")
    print(f.read(5))
    f.close()
except FileNotFoundError:
    print("The file does not exist")


# CREATE A NEW FILE
import os

filename = "myfile.txt"

if os.path.exists(filename):
    print("The file exists")
else:
    print("Create a New File")
    open(filename, "x")


#CHECK IF FILE EXISTS
import os
if os.path.exists("demofile.txt"):
    print("the file exists")
else:
    print("The file does not exist")


#EXCEPTION HANDLING
#example 1
# Exception Handling With Try & Except
print("Exception Handling With Try & Except")
number = input("Enter a number: ")
try:  
    # This code will run if the input is a number
    number = int(number)
    print(number)
except ValueError as err:
    # This code will run if the input is not a number
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")

#example 2
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# example 3(working with files)
try:
    file = open("work.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    if file:
        file.close()

#CUSTOME ERROR HANDLING
class CustomException(Exception):
    pass

def divide_numbers(a, b):
    if b == 0:
        raise CustomException("Division by zero is not allowed.")
    return a / b

try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except CustomException as e:
    print("An error occurred:", str(e))

# Exception Handling using raise
print("Exception Handling using raise")
number = input("Enter a number: ")
try:
    number = int(number)
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    print(number)
except ValueError as err:
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")

# Exception Handling using else
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except AssertionError:
    print("Invalid input. Please enter a number")
else:
    # This code will run if the input is a number
    print(number)


#another example on custom exception handling
class AgePermissionException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"AgePermissionException: Age {self.age} does not meet the required permission."


def check_age_permission(age):
    if age < 18:
        raise AgePermissionException(age)
    else:
        print("Access granted. You have the required age permission.")


try:
    user_age = int(input("Enter your age: "))
    check_age_permission(user_age)
except AgePermissionException as e:
    print(str(e))


