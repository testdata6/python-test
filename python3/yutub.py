#!/usr/bin/python


## Basic Translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEGaeg":
            translation = translation + "j"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a value: ")))  # If type gon it will print "jon"
