#!/usr/bin/python

## Reading files
## Use open() function to read your files from the outside of python.
## We can open this file with below modes
## r  = read the information
## w  = write the information
## a  = Append information
## r+ = read and write

## close() Function is use to close your open file.

#-------------------
## In this example,try to read file "employees.txt"

#open("employees.txt", "r")
## store in variable.
employee_file = open("hello-string.py", "r")
print(employee_file.readable()) # Check the condition and print True if it is in read mode else print false. (It wont continue if the condition is false.)
print(employee_file.read()) # It will read and print all the content of the file.
print(employee_file.readline())
employee_file.close()

#-------------------
print("---------------")

employee_file = open("hello-string.py", "r")
print(employee_file.readline())     # Print first line of the file
employee_file.close()

#-------------------
print("---------------")

employee_file = open("hello-string.py", "r")
print(employee_file.readline())     # Print first line of the file
print(employee_file.readline())     # Print second line of the file
employee_file.close()

#-------------------
print("---------------")
employee_file = open("hello-string.py", "r")
print(employee_file.readlines())    # print all the lines in arry elements
employee_file.close()

#-------------------
print("---------------")
employee_file = open("hello-string.py", "r")
print(employee_file.readlines()[1])     # To print specific element from the arry
employee_file.close()