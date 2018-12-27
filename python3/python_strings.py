#!/usr/bin/python
a = " Hello, World!"
x = "a,b,c,d"
print (a) # Print all string value
print(a.index("H")) # Print index function number of the first string chracter.
print (a[1]) # Get the character at position/Index 1)
print (a[1:6]) # Get the characters from position/index 1 to position 6
print (len(a))# The len() function method returns the length of a string: (Including white space)
print (a.strip()) # The strip() function method removes any whitespace from the beginning or the end:
print (a.upper()) # The upper() function Translate string value to Upper case, like 'tr' command
print (a.lower()) # The lower() function Translate string value to Lower case, like 'tr' command
print (a.replace("o", "O")) # The replace() function method replaces a string with another string:
print (x.split(","))    # The split() function print values in array format sperated by "," here.