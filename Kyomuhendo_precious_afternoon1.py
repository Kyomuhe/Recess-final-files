#dictionaries
"""
my_dict = {
    "phone": "iphone",
    "iphone_model": "iphone 14",
    "year":2023,
    "color":["yellow","blue","black"]

}
print(my_dict)
#length of a dictionary

print(len(my_dict))

#data type
print(type(my_dict))

#accessing dictionary items
z=my_dict["phone"]
print(z)
#another method
y=my_dict.get("phone")
print(y)

#using the keys method
w = my_dict.keys()
print(w)

"""

#exercise1: use values methods to return the list of all values in the dictionary 
my_dict = {
    "key1": 10,
    "key2": 20,
    "key3": 30,
    "key4": 40,
    "key5": 50
}

values_list = list(my_dict.values())
print(values_list)

m= list(my_dict.keys())
print(m)
#exercise2:to check if a key exists in the dictionary
my_dict = {
    "key1": 10,
    "key2": 20,
    "key3": 30,
    "key4": 40,
    "key5": 50
}

key = "key3"

if key in my_dict:
    value = my_dict[key]
    print(f"The key '{key}' exists in the dictionary with a value of {value}.")
    print("The key 'key3' exists in the dictionary with a value of " + str(my_dict["key3"]))

else:
    print(f"The key '{key}' does not exist in the dictionary.")

#exercise3:how to change dictionary items,how to update
my_dict = {
    "key1": 10,
    "key2": 20,
    "key3": 30,
    "key4": 40,
    "key5": 50
}

# Update the value of an existing key
my_dict["key3"] = 35

# Add a new key-value pair
my_dict["key6"] = 60

print(my_dict)

#EXERCISE4:how to add dictionary items,how to remove dictionary items
my_dict = {
    "key1": 10,
    "key2": 20,
    "key3": 30
}

# Adding a new key-value pair
my_dict["key4"] = 40


# Removing a key-value pair using the del keyword
del my_dict["key2"]

print(my_dict)

#EXERCISE:how to loop through a dictionary,how to nest dictionaries
for i in my_dict:
    print(i, my_dict[i])

#NUMBER EXERCISE
#convert from int to complex
m=2
x = complex(m)
print(x)

#convert from int to float
num_int = 10
num_float = float(num_int)
print(num_float)

#convert from float to complex
num_float = 3.14
num_complex = complex(num_float)
print(num_complex)

#convert from complex to float
num_complex = 2 + 3j
num_float = num_complex.real
print(num_float)

#Strings
print("Afternoon")
print('Afternoon')

#assign a string to a variable
w="Afternoon"
print(w)

#multiline strings
q= """Iam offering BSSE Year two 
currently doing recess in python, 
datascience,Django"""
print(q)

#Strings as arrays
a = "Afternoon"
print(a[0])

#how to modify strins
print(a.lower())
print(a.upper())

#STRING EXERCISE 
# use len() function to determine the length of the string
my_string = "Hello, world!"
length = len(my_string)
print(length)

#use an example showing the use of loops in a string
my_string = "Hello"
for char in my_string:
    print(char)

#slicing of strings
my_string = "Hello, world!"
substring = my_string[7:12]
print(substring)


#booleans
print(20<10)
print(30==20)
print(30>=10)

print(bool(15))

r="Livingstone"
z=30

print(bool(r))
print(bool(z))


#EXERCISE ON BOOLEANS
#use a condition to show how to use booleans

x = 5
y = 10

is_greater = x > y

if is_greater:
    print("x is greater than y")
else:
    print("x is not greater than y")

#another example
is_raining = True

if is_raining:
    print("Remember to take an umbrella!")
else:
    print("No need for an umbrella.")


#formart strings -works when one wants to combine a string to a number 
age =20
#name ="my name is prcious kay"+age
name ="my is precious kay and iam {}"
print(name.format(age))

#another example on formarting strings using multiple variables
quantity = 5
price = 20000
tax = 0.35
txt= "precious kay has bought {} pices at {} shs and the tax imposed is {}"

print (txt.format(quantity,price,tax))
