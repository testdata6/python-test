#!/usr/bin/python


## 2D list in loop

alpha_grid = [
    ["John", "Jony", "Janardan"],   #0 Element have 3 Element
    ["Amar", "Akbar", "Anthony"],   #1 Element have 3 Element
    ["Ram", "Sham"],                #2 Element have 2 Element
    ["GOT"]                         #3 Element have 1 Element
]

print(alpha_grid)   # Print all elements in single line
print(alpha_grid[0][1]) # Print Jony
print(alpha_grid[3][0]) # Print GOT

#Print all elements by row by column
for row in alpha_grid:
    print(row)