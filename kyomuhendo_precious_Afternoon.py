#sets
#printing the values of a set
setone = {"rice","matooke","irish","irish"}
print(setone)

#getting the length of a set
my_set = {1, 2, 3, 4, 5}
set_length = len(my_set)
print("The length of the set is:", set_length)#output:The length of the set is: 5

#accessing items of a set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

#adding items to a set
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)
print(my_set)#output:{1, 2, 3, 4, 5}

#adding two sets together
set1 = {1, 2, 3}
set2 = {4, 5, 6}
combined_set = set1.union(set2)
print(combined_set)

#different datatypes in sets 
#set with integers and strings
my_set = {1, 2, "apple", "banana"}
print(my_set)#output:{1, 2, 'apple', 'banana'}

#Set with floating-point numbers:
my_set = {3.14, 2.718, 1.618}
print(my_set)#output:{1.618, 2.718, 3.14}

#Set with boolean values:
my_set = {True, False}
print(my_set)#output:{False, True}

#Set with mixed data types:
my_set = {1, 2.5, "apple", True}
print(my_set)#output:{1, 2.5, 'apple', True}


#TUPLES IN PYTHON
#tuple
phones =("techno","iphone","sumsang","techno")
print(phones)#output:('techno', 'iphone', 'sumsang', 'techno')

print(type(phones))#output:<class 'tuple'>

#adding elements of one tuple to another
laptops =("Dell","HP","Acer")
laptop =("Apple",)
laptops += laptop
print(laptops) #output:('Dell', 'HP', 'Acer', 'Apple')

#adding two tuples together
Newstock = laptops+laptop
print(Newstock)#output:('Dell', 'HP', 'Acer', 'Apple', 'Apple')

#looping through a tuple
for y in phones:
    print(y)
#using len() on tuples
# Creating a tuple
my_tuple = ("apple", "banana", "cherry", "date")

# Using len() to get the length of the tuple
tuple_length = len(my_tuple)

# Printing the length
print("The length of the tuple is:", tuple_length) #output:The length of the tuple is: 4

#tuples showing different datatypes
my_tuple = (10, "apple", 3, "banana")

# Accessing elements of the tuple
print(my_tuple[0])  # Output: 10
print(my_tuple[1])  # Output: "apple"
print(my_tuple[2])  # Output: 3
print(my_tuple[3])  # Output: "banana"

my_tuple = (2.5, "Hello", [1, 2, 3], ("a", "b", "c"))

# Accessing elements of the tuple
print(my_tuple[0])  # Output: 2.5
print(my_tuple[1])  # Output: "Hello"
print(my_tuple[2])  # Output: [1, 2, 3]
print(my_tuple[3])  # Output: ("a", "b", "c")







