#classes, polymorphism ,encalpsulation

#ASSIGNMENT
#show encapsulation with employee information to give increametation to give pay 
#increamentation ( salary with employee information to new_salary)e.g from 850000 to 1000000

class Employee1:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def give_increment(self, increment_amount):
        self.__salary += increment_amount

# Creating an employee object
employee = Employee1("John Doe", 850000)

# Getting the current salary
current_salary = employee.get_salary()
print("Current Salary:", current_salary)

# Incrementing the salary until it reaches 1000000
increment_amount = 150000
while employee.get_salary() < 1000000:
    employee.give_increment(increment_amount)

# Getting the final salary
new_salary = employee.get_salary()
print("New Salary:", new_salary)


#Example 1
class Car:
    def __init__(self,make,model,year) :
        self.make=make
        self.model=model
        self.year=year

    def start_engine(self):
        print("engine started")

    def stop_engine(self):
        print("engine stopped")


my_car = Car("toyota","corola",2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

  #Example 2: Bank account
class BankAccount1:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} units. New balance: {self.balance} units.")

    def show_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current balance: {self.balance} units.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance} units.")

account = BankAccount1("12345", 1000)  # Creating an account with account number "12345" and initial balance of 1000 units

account.show_balance()  # Output: Account Number: 12345  Current balance: 1000 units.

account.withdraw(500)  # Output: Withdrew 500 units. New balance: 500 units.
account.show_balance()  # Output: Account Number: 12345  Current balance: 500 units.

account.deposit(1000)  # Output: Deposited 1000 units. New balance: 1500 units.
account.show_balance()  # Output: Account Number: 12345  Current balance: 1500 units.


#Example3:calculate area and perimeter of a Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(5, 10)  # Creating a rectangle with length 5 and width 10

area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

#Example4: University student:
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Course: {self.course}")


stud = Student('kyomuhendo Precious','year 2','BSSE')
stud.print_info()

#exercise 1
# calculate the area and the circumference of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(5)  

area = circle.calculate_area()
circumference = circle.calculate_circumference()

print(f"Area: {area}")
print(f"Circumference: {circumference}")

#exercise 2
# calculate and display employee bonuse(15) of salary ,employee1:150000,employee2:250000

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary *(15/100)
    
    def display_bonus(self):
        print(f"Bonus: {self.calculate_bonus()}")

employee1 = Employee("John", 150000)  
employee2 = Employee("Alice", 250000) 

employee1.display_bonus()
employee2.display_bonus()

#Encalpsulation

    
#Exercise3: convert temperature(37 celsius) from celsius to Fahrenheit

class TemperatureConverter:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32


temperature = TemperatureConverter(37)  # Creating a TemperatureConverter object with Celsius value 37

fahrenheit = temperature.get_fahrenheit()

print(f"The temperature in Fahrenheit is: {fahrenheit}°F")

# Attempting to access the mangled attribute directly
#print(temperature.__celsius)






