#!/usr/bin/python

## Basic Translator

def translate(phrase):  # The string "gon" comes in array list "g", "o" and "n"
    translation = ""
    for letter in phrase:   # 1) First letter is "g": 5) Second letter is "o"
        if letter in "AEGaeg":      # 2) Having "g", so condition is true: 6) condition is false
            translation = translation + "j"     # 3) replace with "j" in element and store variable
        else:
            translation = translation + letter  # 7) "o" store in variable
    return translation  # 4) Output element comes here "j": 8) "o" will return in output.

print(translate(input("Enter a value: ")))  # If type gon it will print "jon"
