#!/usr/bin/python

## Making own dictitonries

monthConv = {
    #kayname:Value  #(Keyname should be unique)
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Augest",
    "Sep": "Septermber",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    #-----------
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "Augest",
    "9": "Septermber",
    "10": "October",
    "11": "November",
    "12": "December",
}

print(monthConv["Jan"])     # If keyname is incorrect then it will error
#OR
print(monthConv.get("Feb")) # If keyname is incorrect then it will print None instead of error the code
print(monthConv.get("MAR")) # Print None
print(monthConv.get("APR", "Not a valid keyname"))  # Print message instead of None.


print(monthConv["5"])