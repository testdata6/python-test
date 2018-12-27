#!/usr/bin/python

## example for game program


confirm = ""
print("Are you sure you want to continue to install software..?")

while confirm != "YES":
    confirm = input("Enter (YES/NO): ")
    if confirm == "NO":
        print("The script is exited")
        break
    elif confirm == "YES":
        print("[ Done ] Software is installed now")
