#!/usr/bin/python

## Default function true and false
#simple if
is_male = True

if is_male:
    print("Yes, Your are a male")  # If condition is True
#-------------

#if and else
is_female = False

if is_female:
    print("Yes, You are a female")   # If condition is True
else:
    print("No, You are not female")  # If condition is False

#-------------

#OR Operator with if
is_male = True
is_cool = False

if is_male or is_cool:
    print("He is a male and cool")
else:
    print("You neither male or cool")
#-------------

#AND Operator with if
is_male = True
is_cool = False

if is_male and is_cool:
    print("You are a male and cool")
else:
    print("You neither male or cool")

#-------------
print("============================")
#AND, NOT Operator with Nested IF
is_male = True
is_cool = False

if is_male and is_cool:
    print("You are a male and cool")
elif is_male and not(is_cool):
    print("You are a male But NOT cool")
else:
    print("You neither male or cool")
#-------------

print("============================")
#AND, NOT Operator with multile Nested IF
is_male = False
is_cool = True

if is_male and is_cool:
    print("You are a male and cool")
elif is_male and not(is_cool):
    print("You are a male But NOT cool")
elif not(is_male) and is_cool:
    print("You are NOT male but you are COOL")
else:
    print("You neither male or cool")