#!/usr/bin/python

## Basic Translator. AEG/aeg will translate to "g".

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEG":
            translation = translation + "J"
        elif letter in "aeg":
        ## OR
        #elif letter.lower() in "aeg":
            translation = translation + "j"
        else:
            translation = translation + letter
    return translation

#print(translate(input("Enter a value: ")))


#----- OR

def translate2(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeg":
            if letter.isupper():
                translation = translation + "J"
            else:
                translation = translation + "j"
        else:
            translation = translation + letter
    return translation

print(translate2(input("Enter a value: ")))


