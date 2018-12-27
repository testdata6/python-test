#!/usr/bin/python

## 2D list in loop

service = [
    ["http", "ftp", "DNS"],   #0 Element have 3 Element
]

print("Restarting all servers:")
for index in range(len(service[0])):
    print(service[0][index])

