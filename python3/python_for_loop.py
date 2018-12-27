#!/usr/bin/python

## print numbers 1 to 9.
for num in "123456789":
    print(num)

## print character.
for letter in "john":
    print(letter)

## print numbers 1 to 10.
for num in "1", "2", "3", "4", "5", "6", "7", "8", "9", "10":
    print(num)
#OR
## print numbers 1 to 10. using range funcation
for num in range(1, 11):
    print(num)
#OR
## print numbers 1 to 10. using Arrey/list.
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for num in num_list:
    print(num)

## print numbers 0 to 5. using range funcation
for num in range(6):
    print(num)

## To print word by using Array and rnage and len function.
name_list = ["John", "Jony", "Janardan"]
for name in name_list:
    print(name)
#OR

name_list = ["Amar", "Akbar", "Anthony"]    # index lenth 3
for name in range(len(name_list)):  # range function count from 0 to 2 by lenth number 3.
    print(name_list[name])

name_list = ["Amar", "Akbar", "Anthony"]    # index lenth 3
for name in range(1, len(name_list)):  # Print all array list from index 1.
    print(name_list[name])


## For loop with arry and if statment.
name_list = ["Amar", "Akbar", "Anthony"]
for index in range(3):
    if index == 0:
        print("This is first element:", name_list[index])
    else:
        print("Its NOT first Element", name_list[index])

## how to make Exponet function
def rais_to_power (base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num  # 1*3=3*3=9, 1*2=2*2=4*2=6*2=8*2=16
    return result

print(rais_to_power(3, 2))  #3x3=9
print(rais_to_power(2, 4))  #2x2x2x2=16