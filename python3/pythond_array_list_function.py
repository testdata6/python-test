#!/usr/bin/python

## In python list is similar to Array list.
os = ["RedHat", "Unix", "Fedora", "Ubuntu", "Kali"]
version = ["7.1", "7.2", "22", "16.4", "Fedora"]
#index:  0        1        2        3   ## Above index list. (indexing from front)
#index:  -4       -3       -2       -1  ## Negative index list. (indexing from back)

# Print all the element of the list
print(os)

# append function use to append new element in your array list in the end.
print("Using append function")
os.append("Mint")   # append new element in a end of the list
print(os)           # print all element of list

# insert function use to insert a new index with new element anyware in the array list
print("Using index function")
os.insert(1, "MicroSoft")   # Insert new element with new index position
print(os)

# index function use to print index number of the element
print("Using index function")
print(os.index("MicroSoft"))

# remove function use to remove element from the list
print("Using remove function")
os.remove("Unix")   # remove element
print(os)

# extend function use to extend your existing array list using another array list.
print("Using extend function")
os.extend(version)  # combine both array list.
print(os)           # Print all the elements/values

# clear function use to clear all the element from the list. To make empty your array.
print("Using clear function")
version.clear()
print(version)

# count function use to count the number of element in the list
print("Using count function")
print(os.count("Fedora"))
print(os.count("Ubuntu"))

# sort function use to sort alphabeticaly/numberic in assending order
print("Using sort function")
os = ["RedHat", "Unix", "Fedora", "Ubuntu", "Kali"]
num1 = [5, 3, 4, 2, 1]
os.sort()
num1.sort()
print(os)
print(num1)


# reverse function use to reverse format list.
print("Using reverse function")
os = ["RedHat", "Unix", "Fedora", "Ubuntu", "Kali"]
num2 = [2, 1, 3, 4, 5]
num1.reverse()
num2.reverse()
os.reverse()
print(num2)
print(num1)
print(os)

# copy function use to make another array list using existing array list.
print("Using copy function")
os = ["RedHat", "Unix", "Fedora", "Ubuntu", "Kali"]
os2 = os.copy()
print(os2)