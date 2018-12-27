#!/usr/bin/python

##NOTE: # In Python 2.x input() is designed to return numbers, int or float depending on the input from the user, you can also enter variable names

### Example-1
print("Enter your First name:")
x = input()
##OR
#x = raw_input()

y = input("Enter your Mid Name:")   # Another method to print and input value
##OR
#y = raw_input("Enter your Mid Name:")

print("My First Name is: " + x)
print("My Full Name is: " + x, y)
#--------------------------
##### Example-2 - Arithmatic operation

## Interger value addition with input function:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result1 = num1 + num2       # Default behaviour from input is string variable.
result2 = int(num1) + int(num2)      # Convert string to int, so that it will do addition.
print (result1)     # Print combine values in string
print (result2)     # Print addition value
#------

## Float value addition with input function:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result2 = float(num1) + float(num2)      # Convert string to int, so that it will do addition.
print (result2)     # Print addition value
#------