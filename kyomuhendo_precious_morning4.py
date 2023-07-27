#ASSIGNMENT
# Create a receipt printing program with GUI Interface ,
import tkinter as tk
from tkinter import messagebox

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printing Program")

        self.items = []
        self.prices = []
        self.amounts = []

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.grid(row=0, column=0, padx=5, pady=5)

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=2, padx=5, pady=5)

        self.item_entry = tk.Entry(root)
        self.item_entry.grid(row=1, column=0, padx=5, pady=5)

        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=2, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.receipt_text = tk.Text(root, width=30, height=10)
        self.receipt_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.print_button = tk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.print_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def add_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        amount = self.amount_entry.get()

        if item and price and amount:
            self.items.append(item)
            self.prices.append(float(price))
            self.amounts.append(int(amount))

            self.receipt_text.insert(tk.END, f"{item}: ${price} x {amount}\n")

            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please enter item, price, and amount.")

    def print_receipt(self):
        if self.items and self.prices and self.amounts:
            total_amount = sum(price * amount for price, amount in zip(self.prices, self.amounts))
            receipt = "\n".join(f"{item}: ${price} x {amount}" for item, price, amount in zip(self.items, self.prices, self.amounts))
            receipt += f"\nTotal: ${total_amount}"

            self.receipt_text.delete(1.0, tk.END)
            self.receipt_text.insert(tk.END, receipt)

            messagebox.showinfo("Receipt", "Receipt printed successfully.")
        else:
            messagebox.showwarning("Error", "Please add items, prices, and amounts before printing the receipt.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptApp(root)
    root.mainloop()

#Exercise 1
#Demonstrate using inherritance to calculate area and perimeter of circle and rectangle 
#respectively (Shape: circle)

import math

class Shapes:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

class Circles(Shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangles(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

circle = Circles(5)
print("Circle - Area:", circle.calculate_area())
print("Circle - Perimeter:", circle.calculate_perimeter())

rectangle = Rectangles(4, 6)
print("Rectangle - Area:", rectangle.calculate_area())
print("Rectangle - Perimeter:", rectangle.calculate_perimeter())

#Exercise 2
#Demostrate abstraction using calculating area of a circle and rectangle 

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(3, 4)

# Calculate and print the areas
print("Area of the circle:", circle.calculate_area())
print("Area of the rectangle:", rectangle.calculate_area())


#inherritance
class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating ...")    

class Dogs(Animals):
    def bark(self):
        print(f"{self.name} is barking...")

class Cats(Animals):
    def meow(self):
        print(f"{self.name} is meowing...")

#create Animal objects
animal = Animals("Generic Animal")
dog = Dogs("Bob")
cat = Cats("whitty")

animal.eat()
dog.eat()#this shows that the subclasses can acces the methods of a super class
cat.eat()

dog.bark()
cat.meow()

#Example 2
class Vehicle:
    def __init__(self,brand,color):
        self.brand =brand
        self.color = color

    def display_info(self):
        print("Brand: " + self.brand)
        print("Color: " + self.color)
    def move(self):
        print("the vehicle is moving")


class Car(Vehicle):
    def __init__(self,brand,color,num_wheels):
        super().__init__(brand,color)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print("Number of wheels: " + str(self.num_wheels))

    def honk(self):
        print("honking the horn")

#create a car object
my_car = Car("toyota","Red",4)
print("Brand: " +my_car.brand)

# invoke car methods
my_car.display_info()
my_car.honk()
my_car.move()

# MULTIPLE INHERRANCE
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

class Flyable:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying...")

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
     
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

# Create a Bird object
my_bird = Bird("Sparrow", "Passerine")

# Invoke Bird methods
my_bird.display_info()
my_bird.eat()
my_bird.fly()

# Method overriding
class Student:
    def make_sound(self):
        print("Animal is making a sound!")

class Dog(Student):
    def make_sound(self):
        print("Dog is barking!")

class Cat(Student):
    def make_sound(self):
        print("Cat is meowing!")

def make_animal_sound(animal):
        animal.make_sound()

#create objects
student = Student()
dog = Dog()
cat = Cat()

# Calling make_animal_sound function
make_animal_sound(student)
make_animal_sound(dog)
make_animal_sound(cat)

#polymorphism -- allows you to write code that can work with different objects
# Method overiding allows a method to have different implementations, it occurs in inherritance
# Method overloading allows a class to have mutiple methods with the same name but with different parameters

# Example of method overloading
class MathOperations:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c


# Create an instance of the MathOperations class
math_ops = MathOperations()

# Call the add method with different numbers of arguments
print(math_ops.add(2, 3))            # Uses the add method with 2 parameters
print(math_ops.add(2, 3, 4))         # Uses the add method with 3 parameters


# Abstraction, it allows you to forcus on esstential features and hide them from unneccessary details
# Example:
from abc import ABC,abstractmethod
class University(ABC):
    @abstractmethod
    def get_students(self):
        pass
    
    @abstractmethod
    def get_courses(self):
        pass

class Course(University): 
    def get_students(self):
        print("Students: ")

    def get_courses(self):
        print("Courses: ")  

# creating the objects
course = Course()
course.get_students()
course.get_courses()

# a more advanced detail earns you more point






























