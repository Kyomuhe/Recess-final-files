#control flow
#conditional statements(if elif else)
age =100
if age<18:
    print("you are under age")
elif age >=18 and age < 65:
    print("you are an adult")
else :
    print("you are  a citzen")

#loops(for ,while)
#for
sequence =(1,2,3,4,5)
for i in sequence:
    print (i)

#while
x=0
while x<=5:
    print(x)
    x+=1

#Exercise
fruits = ["apple", "banana","orange","berrys"]
fruit_count = 0
while fruit_count < len(fruits):
    print(fruits[fruit_count])
    fruit_count += 1

#break statement
for number in range(1,10):
    if number ==3:
        break
    print (number)

#continue
for number in range(1,10):
    if number ==3:
        continue
    print (number)

#Exercise
names =["precious","kay","luis","bob"]
for name in names:
    if name =="kay":
        continue
    print (name)

names =["precious","kay","luis","bob"]
for name in names:
    if name =="kay":
        break
    print (name)

#exception handling ,using try except and finally
#Exercise
try:
    dividend = 10
    divisor = 0
    result = dividend / divisor
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This code will always execute, regardless of any exceptions.")


#using a dictionary
emotion = {
    'happy':"happy",
    'sad' :"iam sad",
    'angry':"im angry"

 }
user = input("how are you feeling today")
user =user.lower()
if user in emotion:
    print(emotion[user])
else :
    print ("iam sorry i dont understand your emotions")

    
#EXERCISE -(a program that prompts students to rate their mental health using a range(1,10))
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
