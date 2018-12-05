#!/usr/bin/python

##Membership operators are used to test if a sequence is presented in an object:
   # in 	Returns True if a sequence with the specified value is present in the object	x in y	
   # not in	Returns True if a sequence with the specified value is not present in the object	x not in y

#------------------

opt="in operators"
print ("============= %s" %opt)

a=["banana", "apple", "mango"]
print ("apple" in a)	# True - returns True because a sequence with the value "apple" is in the list

x="john"
print ("john" in x)	# True

y="bobb"
print ("bob" in y)	# True

z="alice"
print ("blice" in z)	# False	- returns False because a string "blice" is not in the list

#---------------
opt="not in operators"
print ("============= %s" %opt)

a=["banana", "apple", "mango"]
print ("apple" not in a)	# False - returns False because a sequence with the value "apple" is in the list

x="alice"
print ("bob" in z)		# True - returns False because string "bob" is not in the list 

#---------------

########## Other example 
## iF
print ("=============")
fruits=["mango", "apple", "banana"]
if "apple" in fruits:
  print "Apple is there"
