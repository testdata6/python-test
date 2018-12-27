#!/usr/bin/python

## While loop

## Print number from 1 to 10
i = 1
while i <= 10:
    print(i)
    #i = i + 1
    ###OR
    i += 1

print("Done with loop")
#------------------------

## Print number from 1 to 5 from 1 to 10.
## Break statment in while loop

i = 1
while i <= 10:  # Until condition wont false, checking false condition.x
    if i > 5:   # Checking true condition to break
        break
    print(i)
    i += 1
print("End Loop")

#---------------------------------

## Print number from 1 to 10 except 5.
## Continue statment in while loop

i = 0
while i <= 9:  # Until condition wont false, checking false condition.x
    i += 1
    if i == 5:   # Checking true condition to break
        continue
    print(i)
print("End Loop")