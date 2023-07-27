"""comments:they are used to further explain the purpose of code and make code readable,
there are two types of comments"""
 #this is a single line comment
"""
this is a multi line comment
"""
#variables
name="precious"
#in the above example the value "precious" is stored in the valriable callled name

#printing data
print('precious kay yeeh!!!!')

#Data types
#Integer (int):
x = 10
print(type(x))#output:<class 'int'>
#Float (float): Used to represent decimal numbers.
y = 3.14
print(type(y))

#String (str): Used to represent a sequence of characters.
name = "John"
print(type(name))#output:<class 'str'>
#Boolean (bool): Used to represent logical values, either True or False.
is_true = True
print(type(is_true))#output:<class 'bool'>
#Sequence types

#List (list): Used to store a collection of items, which can be of different data types.
numbers = [1, 2, 3, 4, 5]

names= ["precious","kay","beteise","frank","jackie"]
print(names)
#operations on lists
print(len(names))#output:5

print(type(names))#output: <class 'List'>

print(names[0])#output:precious

print(names[-1])#output:jackie

print(names[2:4])#output:['beteise', 'frank']

print(names[:4])#output:['precious', 'kay', 'beteise', 'frank']
names.insert(0,"kial")
print(names)#output:['kial', 'precious', 'kay', 'beteise', 'frank', 'jackie']

names.append("kishala")
print(names)#output:['kial', 'precious', 'kay', 'beteise', 'frank', 'jackie', 'kishala']

names.pop(2)
print(names) #output:['kial', 'precious', 'beteise', 'frank', 'jackie', 'kishala']

#Tuple (tuple): Similar to a list, but immutable (cannot be modified once created).
coordinates = (10, 20)

#Dictionary (dict): Used to store key-value pairs, where each key is unique.
person = {'name': 'John', 'age': 30}

#Set (set): Used to store unique elements in an unordered manner.
unique_numbers = {1, 2, 3, 4, 5}

#None (NoneType): Represents the absence of a value.
result = None


#STUDENT MENTAL HEALTH ASSESMENT
responses = {
    "1": "I'm sorry to hear that. Please consider reaching out for support.",
    "2": "I hope things get better for you soon. Take care of yourself.",
    "3": "It sounds like you're going through a tough time. Remember, you're not alone.",
    "4": "I'm here for you. Don't hesitate to ask for help if you need it.",
    "5": "Take some time for self-care. You deserve it.",
    "6": "That's good to hear. Keep taking care of your mental health.",
    "7": "I'm glad you're doing well. Keep up the positive mindset.",
    "8": "Great! Keep up the good work and continue prioritizing your mental well-being.",
    "9": "Fantastic! It's wonderful to hear that you're feeling mentally strong.",
    "10": "That's excellent! Keep thriving and remember to support others around you."
}

print("Welcome to the Student Mental Health Assessment")
print("----------------------------------------------")

while True:
    rating = input("Please rate your mental health from 1 to 10 (1 = very low, 10 = very high): ")
    
    if rating.lower() == "exit":
        print("Thank you for using the Student Mental Health Assessment. Goodbye!")
        break
    
    if rating.isdigit() and 1 <= int(rating) <= 10:
        if rating in responses:
            print(responses[rating])
        else:
            print("Invalid rating. Please try again.")
    else:
        print("Invalid rating. Please enter a number between 1 and 10.")
    
    print()
