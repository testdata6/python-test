#!/usr/bin/python

## In python list is similar to Array list.
os = ["RedHat", "Unix", "Fedora", "Ubuntu", "Kali"]
#index:  0        1        2        3   ## Above index list. (indexing from front)
#index:  -4       -3       -2       -1  ## Negative index list. (indexing from back)
#To print all list/elements
print(os)

# To print "Redhat" use index number 0
print(os[0])    # print RedHat

# To print "Unix" use index number 1
print(os[1])    # print Unix

# To print last element of the list
print(os[-1])   # print Kali

# To print second last element use negative index number.
print(os[-2])   # print Ubuntu

# To print all the element after this index.
print(os[1:])   # print "Unix", "Fedora", "Ubuntu", "Kali"

# To print element in range of index. use current index and previous index of last.
print(os[1:3])   # print "Unix", "Fedora" (use only 1,2 index and 3rhd will skip)


# To change the value of index position
os[1] = "CentOS"    # Value changed for index 1
print(os[1])        # Print Centos