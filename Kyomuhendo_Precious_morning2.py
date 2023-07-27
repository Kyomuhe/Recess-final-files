#tkinter learn
#create a simple calculator program with a GUI interface , make your title of the calculator 
#program window with your name e.g "precious kay simple calculator"
import tkinter as tk

# Function to perform calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Creating the main window
window = tk.Tk()
window.title("Precious kyomuhendo Simple Calculator")

# Creating an entry widget for input and display
entry = tk.Entry(window, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating buttons for numbers and operators
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button in buttons:
    text, row, column = button
    btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 12),
                    command=lambda text=text: entry.insert(tk.END, text))
    btn.grid(row=row, column=column, padx=5, pady=5)

# Creating a button for calculation
calculate_btn = tk.Button(window, text="Calculate", width=20, height=2,
                          font=("Arial", 12), command=calculate)
calculate_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Creating a button for clearing the entry widget
clear_btn = tk.Button(window, text="Clear", width=20, height=2,
                      font=("Arial", 12), command=clear)
clear_btn.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

# Run the main event loop
window.mainloop()


#Basic operators and expressions (input output operations)
"""
Arithmetic operators
+Addition
-Subtraction
*Multiplication
/Division
%Modulus
//Divide (return the quotient with out the remainder)
** Exponentiation
Comparison operators
==Equal to
!=Not equal !==
>Greater than
<Less than
>=Greater than or equals to
<=Less than or equal to

logical operators
Logical AND 'and'
Logical OR 'or'
LOgical NOT 'not'

Assignment Operators
Assign value: '='
Add value: '+'
Add and Assign value: '+='
Subtract and assign: '-='
multiply and assign valu:'*='
Divide and assign:'/='
Modulus and assign value: '%='
Exponenetiate and assign value :'**='

Membership operator
In: 'in' operator: checks if a value exists in a sequence
Not in: 'not in ' operator:checks if a value does not exist in a sequence

Identity operators
Is: 'is' operator: checks if two values are the same
Is not: 'is not' operator: checks if two values are not the same
"""
# Examples of arithmetic operators
#Addition
x = 20+30
print(x)
#Subtraction
z = 20-30
print(z)
#Multiplication
m = 20*30
print(m)
#Division
b= 20/30
print(b)
#Divide
a = 20//30
print(a)
#ModulusS
f = 5%2
print(f)
#Exponentiation
d = 2**4
print(d)

#Examples of comparison
a=15
b=9
#Greater than
if a>b:
    print('a is greater than b')
    print(a>b)

#less than
if a<b:
    print ('a is less than b')
    print(a<b)

#greater than or equal to
if a>=b:
    print ('a is greater than or equal to b')
    print(a>=b)

#less than or equal to 
if a<=b:
     print ('a is less than or equal to b')
     print(a<=b)

#Equal to 
if a==b:
    print( 'a is == b')
    print(a==b)

#not equal to
if a!=b:
    print('a is not equal to b')
    print(a!=b)


#Examples of logical operators
#Logical operators
a = True
b = False
#Logical AND
if a and b:
    print ('a and b is True')
    print(a and b)
        
#Logical OR
print(a or b)
#Logical NOT
print(not a)
print(not b)

#Assignment operator
#compound assignment operators
a=5
#Add and assign operator
a +=5
print(a)
#subtract and assign
v=10
v -=5
print(v)

#multiply and assign
k=10
k *=10
print(k)

#Divide and assign
q=10
q /=10
print(q)
# MOdulus and Assign
j=5
j %=2
print(j)

#Exponenetiation and Asiign
m=3
m **=4
print(m)

#Membership assignment operators
cars =['jeep','tesla','bmw','roll royce']
if 'jeep' in cars:
    print('jeep is in the list')
    print('tesla' in cars)
    print('toyota' in cars)

#is operator 
x=10
y=10

print(x is y)
print(x is not y)
print(x==y)
print(x!=y)
print(x<y)
print(x<=y)

#list
#is not operator
z=[1,2,3,4,5,6,7]
w=[1,2,3,4,5,6,7]
print(z is not w)
print(z is w)

#Bitwise operators
"""
are used to perform operations on individual bits on binary numbers 
Bitwise AND('$'): performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR ('|'):performs a bitwise OR operation between the corresponding bits of two integers
Biwise XOR ('^'):
Bitwise NOT ('-'):
Biwise left shift('<<')
Bitwise right shift('>>'):performs a biwise right shift operation
"""
a = 10
b = 20
print("bitwise operators")
#Bitwise operation AND
result = a & b
print(result)
#Biwise OR
a = 5  # binary: 0101
b = 3  # binary: 0011

result = a | b  # bitwise OR
print(result)  # Output: 7 (binary: 0111)

#Bitwise XOR
a = 5  # binary: 0101
b = 3  # binary: 0011

result = a ^ b  # bitwise XOR
print(result)  # Output: 6 (binary: 0110)

#Bitwise NOT
a = 5  # binary: 0101

result = ~a  # bitwise NOT
print(result)  # Output: -6 (binary: 1010 in two's complement)

#Bitwise left shift
a = 5  # binary: 0101

result = a << 2  # bitwise left shift by 2 positions
print(result)  # Output: 20 (binary: 10100)

#Bitwise right shift
a = 20  # binary: 10100

result = a >> 2  # bitwise right shift by 2 positions
print(result)  # Output: 5 (binary: 0101)




































