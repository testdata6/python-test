#!/usr/bin/python

## Try Except - block

## 1st it will execute try: block and then if the execution error or false  then it will execute except: block.
# Here We dont required if and else condition.

#----
## In this example try to input integer/aplphbetic and see what happen
try:
    number = int(input("Enter a number: "))  # Accept only integer and that is the condition.
    print(number)
except:
    print("Invalid value entered")

#-------------------
## In this example try to error your execution.
try:
    value = 10 / 0  # First execution. except: block execute here. wont execute next execution.
    number = int(input("Enter a number: "))  # Second execution.
    print(number)  # third execution
except:
    print("Invalid value entered")

#-------------------
## In this example  Lets try execute except: block based on different errors through.
try:
    value = 10 / 0  # First execution. except: block execute here. wont execute next execution.
    number = int(input("Enter a number: "))  # Second execution.
    print(number)  # third execution

except ZeroDivisionError:
    print("Can not be devide by 0")
except ValueError:
    print("Invalid value entered")

#-------------------
## In this example, Lets try execute except: block based on different errors through. using "as" we print default message as it is.
try:
    value = 10 / 2  # First execution. except: block execute here. wont execute next execution.
    number = int(input("Enter a number: "))  # Second execution.
    print(number)  # third execution

except ZeroDivisionError as error1:
    print(error1)
    print("Can not be devide by 0")
except ValueError as error2:
    print(error2)
    print("Invalid value entered")