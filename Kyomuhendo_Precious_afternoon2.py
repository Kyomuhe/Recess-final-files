# create a list with 5 items(name of people) and write a python program to output the 2nd item
names=["precious","kay","mercy","kyomuhendo","pk"]
print(names[1])
#2.	Write a python program to change the value of the first item to a new value 
names[0] = "beteise"
print(names)
#3.	Write a python program to add a sixth item to the list 
names.append("jackie")
print(names)
#4.	Write a python program to add “Bathel” as the 3rd item in your list 
names.insert(2, "Bathel")
print(names)
#5.	Write a python program to remove the 4th item from the list 
del names[3]
print(names)
#6.	Use negative indexing to print the last item in your list 
print(names[-1])
#7.	Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items. 
my_list = [1, 2, 3, 4, 5, 6, 7]
items_3_4_5 = my_list[2:5]
print(items_3_4_5)
#8.	Write a list of countries and make a copy of it. 
countries = ["USA", "Canada", "UK", "Australia", "Germany"]
countries_copy = countries.copy()
print(countries_copy)
#9.	Write a python program to loop through the list of countries 
for country in countries:
    print(country)

#10.	Write a list of animal names and sort them in both descending and ascending order. 

animal_names = ["Elephant", "Tiger", "Lion", "Giraffe", "Zebra"]
animal_names.sort()  # Sort in ascending order
print("Ascending Order:", animal_names)

animal_names.sort(reverse=True)  # Sort in descending order
print("Descending Order:", animal_names)

#11.	Using the list above, write a python program to output only animal names with the letter ‘a’ in them 
animal_names = ["Elephant", "Tiger", "Lion", "Giraffe", "Zebra"]
animal_names_with_a = [name for name in animal_names if 'a' in name.lower()]
for name in animal_names_with_a:
    print(name)

#12.	Write two lists, one containing your first names and the other your second names. Join the two lists. 
first_names = ["precious", "kay", "mercy", "kyomuhendo", "pk"]
second_names = ["beteise", "jackie", "Bathel", "Jack", "Jackie"]
full_names = first_names + second_names
print(full_names)

#EXERCISE TWO
#1.	Consider the tuple below; x = (“samsung”, “iphone”, “tecno”, “redmi”)  	Write a python program to output your favorite phone bran
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print("My favorite phone brand is:", favorite_brand)

#2.	Use negative indexing to print the 2nd last item in your tuple.  
second_last_item = x[-2]
print("The second last item in the tuple is:", second_last_item)

#4.	Write a python program to add “Huawei” to your tuple. 
x = ("samsung", "iphone", "tecno", "redmi")
new_tuple = x + ("Huawei",)
print("Updated tuple:", new_tuple)

#5.	Write a python program to loop through the tuple above. 
x = ("samsung", "iphone", "tecno", "redmi")
for item in x:
    print(item)

#6.	Write a python program to remove/delete the first item in your tuple. 
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print("Updated tuple:", x)

#7.	Using the tuple() constructor, create a tuple of the cities in Uganda. 
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print("Cities in Uganda:", cities)

#8.	Write a python program to unpack your tuple. 
x = ("samsung", "iphone", "tecno", "redmi")
phone1, phone2, phone3, phone4 = x

print("Phone 1:", phone1)
print("Phone 2:", phone2)
print("Phone 3:", phone3)
print("Phone 4:", phone4)

#9.	Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above. 
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
for city in cities[2:4]:
    print(city)

#10.	Write two tuples, one containing your first names and the other your second names. Join the two tuples. 
first_names = ("precious", "kay", "mercy", "kyomuhendo", "pk")
second_names = ("beteise", "jackie", "Bathel", "Jack", "Jackie")
full_names = first_names + second_names
print(full_names)

#11.	Create a tuple of colors and multiply it by 3. 
colors = ("red", "green", "blue", "yellow", "black")
new_colors = colors * 3
print(new_colors)

#12.	Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5) 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))

#Exercise3 (Sets) 
#1.	Use the set() constructor to create a set of 3 of your favorite beverages. 
beverages = set(["coffee", "tea", "juice"])
print("Favorite beverages set:", beverages)

#2.	Use the correct method to add 2 more items to the beverages set. 
beverages.add("water")
beverages.add("milk")
print("Favorite beverages set:", beverages)

#3.	Given the set below; mySet = {“oven”, “kettle”, “microwave”, “refrigerator”} Check if microwave is present in the set. 
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

#4.	Write a python program to remove “kettle” from the set above. 
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print("Favorite beverages set:", mySet)

#5.	Write a python program to loop through the set above. 
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for beverage in mySet:
    print(beverage)

#6.	Write a set of 4 items and a list of two items. Write a python program to add 
# elements in the list to elements in the set.
set = {"oven", "kettle", "microwave", "refrigerator"}
list = ["coffee", "tea", "juice", "water"]
set.update(list)
print("Favorite beverages set:", set)

#7.	Write two sets, one containing your ages and the other your first names. Join the two sets. 
ages = {25, 30, 35}  
first_names = {"Alice", "Bob", "Charlie"}  

joined_set = ages.union(first_names)

print(joined_set)

#Exercise4 (Strings) 
#1.	Declare two variables, an integer and a string and use the correct method to concatenate the two variables. 
integer_variable = 42
string_variable = "The answer is: "

concatenated_string = string_variable + str(integer_variable)

print(concatenated_string)

#2.	Consider the example below; txt = “      Hello,       Uganda!      
#  ” Output the string without spaces at the beginning, in the middle and at the end.
txt = "      Hello,       Uganda!       "
txt.strip()
replaced =txt.replace(" ","")
print(replaced)

#3.	Write a python program to convert the value of ‘txt’ to uppercase. 
txt = " txt"
print(txt.upper())

#4.	Write a python program to replace character ‘U’ with ‘V’ in the string above. 
txt = "Hello,Uganda!       "
print(txt.replace("U", "V"))

"""5.	Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position. 
y = "I am proudly Ugandan
"""
y = "I am proudly Ugandan"

range_of_characters = y[1:4]  # Get characters from index 1 to index 3 (exclusive of index 4)

print(range_of_characters)


#6.	The piece of code below will give an error when output; x = “All “Data Scientists” are cool!”  Write a python program to correct it.
x = "All \"Data Scientists\" are cool!"

print(x)

"""
Exercise5 (Dictionaries) 
1.	With reference to the dictionary below, write a python program to print the value of the shoe size.  
Add this dictionary to your .py file 
Shoes = { 
 	“brand” : “Nick”,  	“color” : “black”, 
	 	“size” : 40 

""" 
Shoes = { 
     "brand" : "Nick","color": "black", 
         "size": 40 
}
print(Shoes["size"])

#2.	Write a python program to change the value “Nick” to “Adidas” 
Shoes = { 
     "brand" : "Nick","color": "black", 
         "size": 40 
}
Shoes["brand"] = "Adidas"
print(Shoes["brand"])

#3.	Write a python program to add a key/value pair "type”: "sneakers" to the dictionary 
Shoes = { 
     "brand" : "Nick","color": "black", 
         "size": 40 
}
Shoes["type"] = "sneakers"
print(Shoes["type"])

#4.	Write a python program to return a list of all the keys in the dictionary above. 
Shoes = { 
     "brand" : "Nick","color": "black", 
         "size": 40 
}
print(Shoes.keys())
#5.	Write a python program to return a list of all the values in the dictionary above. 
Shoes = { 
     "brand" : "Nick","color": "black", 
         "size": 40 
}
print(Shoes.values())

#6.	Check if the key “size” exists in the dictionary above. 
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")

#7.	Write a python program to loop through the dictionary above. 
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

for key, value in Shoes.items():
    print(key, ":", value)

#8.	Write a python program to remove “color” from the dictionary. 
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

del Shoes["color"]
print(Shoes)

#9.	Write a python program to empty the dictionary above. 
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes.clear()
print(Shoes)

#10.	Write a dictionary of your choice and make a copy of it. 
original_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

copied_dict = original_dict.copy()
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

#11.	Write a python program to show nested dictionaries 
student = {
    "name": "John",
    "age": 20,
    "grades": {
        "math": 90,
        "science": 85,
        "english": 92
    }
}

print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Math Grade:", student["grades"]["math"])
print("Science Grade:", student["grades"]["science"])
print("English Grade:", student["grades"]["english"])

























































































































































































