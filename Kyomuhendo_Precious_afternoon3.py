#Functions
"""
functions group a blocks of code
there is need for code that is clean, reusable, maintainable
def function_name():
"""

def afternoon(f_name,l_name):
    print(f"hello {f_name}  {l_name}")
    print("class starts at 2pm")
    print("they are 100 students")

#calling a function
afternoon("kyomuhendo","precious")

#Arguments and parameters
"""
Arguments are the actual values passed to a function when it is called. 
Parameters are inputs to a function and provide a way to pass values into the 
function. Parameters can be defined in the function definition and used within the function block. Python supports different types of parameters,
including positional parameters, keyword parameters, and default parameters.
"""
#functions that take in multiple parameters
def calculate_sum1(a, b, c):
    return a + b + c
result = calculate_sum1(2, 3, 4)
print(result)  # Output: 9


#another example 
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
result = calculate_sum(2, 3, 4)
print(result)  # Output: 9

result = calculate_sum(1, 2, 3, 4, 5)
print(result)  # Output: 15

#modules
"""
a module is a file that contains Python code, including definitions, statements,
 and functions, which can be used in other Python programs. 
Modules provide a way to organize and reuse code by grouping related functionalities together.
"""
import module
print("printing modules")
print(module.add(8, 4))
print(module.product(8, 4))


#importing a square root and factorial from the module math
from math import sqrt, factorial

#or you can import all: from math import *
print(sqrt(16))
print(factorial(6))

#input and output in python
#input('prompt')
#example 1
name =input("enter your name please!!")
print(f"welcome {name}")

#example 2
number= int(input("enter a value"))
product =number*10
print(product)

#multiple inputs
s,r,w = map(int ,input('enter ur values :').split())
print("the values are:", end=" ")
print(s,r,w)


print(f"updated tuple is : {w}")

#how to capture input from a list
listss =["kay","precious"]
print(f"original list :{listss}")
listss.append(input("enter a new name to be added to the list"))
print(f"updated list : {listss}")

#another example
my_list = list(map(int, input("Enter the list values : ").split()))
my_set = set(map(int,input("Enter the set values : ").split()))

print(my_list)
print(type(my_list))
print(my_set)
print(type(my_set))















































