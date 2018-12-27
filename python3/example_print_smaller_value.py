#!/usr/bin/python

#
def max_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1     # return print value with print() function only
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

# Calling function but wont get return value:
print(max_num(1, 5, 5))     # num1 is smaller (print return value)
print(max_num(5, 5, 2))     # num2 is smaller (print return value)
print(max_num(5, 5, 3))     # num3 is smaller (print return value)
