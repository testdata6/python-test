#!/usr/bin/python

## Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
  # is 	Returns true if both variables are the same object	x is y	
  # is not	Returns true if both variables are not the same object	x is not y

#------------------

opt="is operators"
print ("============= %s" %opt)

print (2 is 2 )	# True

x=2
y=4
print (x is y)	# False
#---------------

opt="is not operators"
print ("============= %s" %opt)

print (2 is not 2 )	# True

x=2
y=4
print (x is not y)	# False
#---------------

######### other examples
#1) if

x=4
y=4
if x is not 2:
  print ("X is not having same value")

if x is not y:
  print ("X and Y are not having same value")
else:
  print ("X and Y are having same value")
