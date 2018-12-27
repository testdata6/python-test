#!/usr/bin/python

## Building a calculator
num1 = float(input("Enter a First number: "))   # To accept decimal and float value
opt = input("Enter a operator: ")
num2 = float(input("Enter a Third number: "))

if opt == "+":
    print(num1 + num2)
elif opt == "-":
    print(num1 - num2)
elif opt == "*":
    print(num1 * num2)
elif opt == "/":
    print(num1 * num2)
else:
    print("Invalid Operator..! Pls Enter a correct operator from the list: [+, -, *, /]")
