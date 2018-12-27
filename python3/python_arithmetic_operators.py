#!/usr/bin/python

### Python Arithmetic Operators
##+	Addition	x + y	
##-	Subtraction	x - y	
##*	Multiplication	x * y	
##/	Division	x / y	
##%	Modulus	x % y	
##**	Exponentiation	x ** y	 
##//	Floor division	x // y
##----------------
## Three different way use Operators

## Printing numbers
print (2)
print (2.0)
print (-2.0)
print (2+2)

#Addition
add=2+2
print ('Total Addition is: %s' %add)

##OR
print (2+2)
##OR
x=2
y=2
print(x+y)
##OR
x=2
y=2
output = x + y
print(output)

#Subtraction
sub=10-5
print ('Total Addition is: %s' %sub)
#OR
print (10-5)


#Multiplication
mul=2*2
print ('Total Addition is: %s' %mul)
#OR
print (2*2)


#Division
div=2/2
print ('Total Addition is: %s' %div)
#OR
print (2/2)

#Modulus: Gives you reminder
mod=2%2
print ('Total Addition is: %s' %mod)
#OR
print (2%2)

## Correct method to do arithmetic operation.
print(2*(2+2))  # Correct method
print(2*2+2)  # Incorrect method


## power function(^): How to Calculate Powers of Numbers
print ('Dooing 3 to the power 2. Output Should be:(3^2 = 3*3 = 9)')
print (pow(3, 2))

## Max function(^): To print largest/max number from the list
print (max(2, 7, 9))   # Print 9 as bigest number

## Max function: To print largest/max number from the list
print(max(2, 7, 9))   ## Print 9 as bigest number

## min function: To print smallest number from the list
print(min(2, 7, 9))   ## Print 2 as smallest number

## Round function: To print round value from the float values.
print(round(3.4))   # print round value 3
print(round(3.8))   # print round value 4

## import "math" to get/access all math function.
from math import *
    # floor funcation to skip point value and print constant value. (import math)
print(floor(3.8))  # Print round figure 3
    # ceil funcation to read point value and print upper value. (import math)
print(ceil(3.8))  # Print round figure 4

    # The square root of a number, is the number that gives n when multiplied by itself. by math import. (import math)
print(sqrt(9))      # Print 9 <= 3*3 <= 3.0
print(sqrt(4096))   # Print 4096 <= 64*64 <= 64.0