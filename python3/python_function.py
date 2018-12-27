#!/usr/bin/python
## Function is the collection of code. "def" is the keyboard to creating a function.

# Creating a simple function
def hi_fun():
    print("Hello World")
# Calling the function.
print("Bye World")
hi_fun()

#-----------------
## Function with single argument/position parameter

def hi_fun2(my_name):
    print("Hello " + my_name)
hi_fun2("Amit")
hi_fun2("John")
#-----------------
## Function with multiple argument/position parameter

def hi_fun3(first_name, last_name):
    print("Hello " + first_name, last_name)
hi_fun3("Amit", "Ganvir")

#-----------------
# Arithmatic function with return statment.
def add(num):
    return num+num+num

print (add(2))
##OR
result = (add(2))
print(result)
#-----------------

