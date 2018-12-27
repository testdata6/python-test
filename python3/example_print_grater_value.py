#!/usr/bin/python

#
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1     # return print value with print() function only
    elif num2 >= num1 and num2 >= num3:
        print("num2 is grater")
        return num2
    else:
        print(str(num3) + " : value of num3 is a grater")
        return num3

# Calling function but wont get return value:
max_num(5, 4, 3)    # num1 is grater
max_num(1, 4, 3)    # num2 is grater
max_num(1, 2, 3)    # num3 is grater

print("----------")
print(max_num(6, 1, 2))     # num1 is grater (print return value)
print(max_num(1, 5, 2))     # num2 is grater (print return value)
print(max_num(1, 2, 4))     # num3 is grater (print return value)
