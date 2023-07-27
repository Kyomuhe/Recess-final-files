#Advanced topics
"""
Regular expressions
Generators and iterators
Decorators
context managers
multithreading and multiprocessing
"""

#Matching and searching
#regex re.match(), re.search, re.findall()
#Example 1 demostrating regex | Match first word , match Group word, match all numbers
import re
text ="hello my name is precious kay, iam a programmer with 15 years of experience"

# match first word
match = re.search(r"\b\w+\b", text)
if match:
    print("Matches:", match.group())

matches = re.findall(r"\d+", text)
print("Matches:", matches)

#Example 2 validate email format or email address
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
#example usage
email ="kyomuhendoprecious84@gmail.com"
email2="kyomuhendoprecious84@gmailcom"

print(validate_email(email))
print(validate_email(email2))

#Generators and Iterators
#'yield' generator
#Iterator '__iter__' "__next__" iterator

#Genartor example
def factorial(n):
    #return the factorial of a number
    if n == 0: 
        return 1
    else:
        return n *factorial(n-1)
    
# print the factorial of a number from 1-10
for i in range(1,10):
    print(factorial(i))


print("using generators")
def factorial_generator(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        yield 1
    # Recursive case: yield intermediate results using generator
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        yield result

# Print the factorial of numbers from 1 to 10
for i in range(1, 11):
    print(next(factorial_generator(i)))


# Example 3 
# Generate functions that yields the square of numbers from 1 to 10
def squares():
    for i in range(1,10):
        yield i**2

squares_iterator = squares()
#print the first 5 squares of numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator))

#ITERATORS
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        element = self.data[self.index]
        self.index += 1
        return element


# Creating an instance of the iterator
my_iterator = MyIterator([1, 2, 3, 4, 5])

# Iterating over the elements using a for loop
for item in my_iterator:
    print(item)

# Output: 1 2 3 4 5
# USING FOR loop IN ITERATORS
trial ={"precious","kay","mercy"}
trial_iterator =iter(trial) 
for i in range(3):
    print(next(trial_iterator)) 

#Decorators @my_decorator
"""
In Python, decorators are a way to modify the behavior of functions
or classes without directly modifying their source code. They allow you
to wrap or modify a function or class by applying additional functionality 
before, after, or around the original code.
"""
#example 1
def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
    return inner

@my_decorator
def outer_decorator():
    print("This is the outer decorator")

outer_decorator()

#example 2
def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

print(greet())

#CONTEXT MANAGERS
"""
In Python, context managers are used to manage resources 
that need to be set up and cleaned up properly. 
They ensure that certain actions are taken before and after a block of code is executed.
"""
from contextlib import contextmanager

# Placeholder functions for acquiring and releasing the resource
def acquire_resource():
    print("Resource acquired")
    return "Resource"

def release_resource(resource):
    print("Resource released:", resource)

@contextmanager
def my_context_manager():
    resource = acquire_resource()  # Acquire the resource
    try:
        yield resource  # Make the resource available within the 'with' block
    finally:
        release_resource(resource)  # Release the resource

# Using the context manager
with my_context_manager() as res:
    # Code inside the 'with' block
    print("Using the resource:", res)

#multithreading and multiprocessing
"""
Multithreading:
Multithreading is a technique that allows multiple threads of execution
to run concurrently within a single process. Each thread represents
an independent flow of execution, and they share the same memory space
"""
#EXAMPLE ON MULTITHREAD
import threading

def print_numbers():
    for i in range(1, 6):
        print("Thread 1:", i)

def print_letters():
    for char in 'ABCDE':
        print("Thread 2:", char)

# Create two thread objects
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

"""
Multiprocessing:

Multiprocessing is a technique that allows multiple processes to run concurrently,
each with its own memory space. Unlike multithreading, multiprocessing takes advantage
of multiple CPU cores and can provide performance improvements for CPU-bound tasks.
"""
#Example on multiprocessing
#Another example
import multiprocessing

def square(number):
    return number * number

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    # Create a Pool of processes
    pool = multiprocessing.Pool()
    
    # Apply the square function to each number in parallel
    results = pool.map(square, numbers)
    
    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()
    
    # Print the squared results
    print("Squared numbers:", results)
