#!/usr/bin/python

## Logical operators are used to combine conditional statements:
  # and 	Returns True if both statements are true	x < 5 and  x < 10	
  # or	Returns True if one of the statements is true	x < 5 or x < 4	
  # not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

#------------------

opt="AND"
print ("============= %s" %opt)

print (2 == 2 and 4 > 2 )	# True

x=2
y=2
z=4
print (x == y and y > z)	# False
#---------------
opt="OR"
print ("============= %s" %opt)

print (2 != 2 or 4 > 2 )	# True

x=2
y=2
z=4
print (x == y or y > z) 	# False
#---------------
opt="not"
print ("============= %s" %opt)
#returns False if the result is true

print (not(2 == 2 and 4 > 2) )	# False
print (not(2 > 5 and 5 == 5) )  # True

x=2
y=2
z=4
print (not(x == y and y > z)) # True
#---------------
