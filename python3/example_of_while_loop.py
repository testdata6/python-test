#!/usr/bin/python

## example for game program


secret_word = "batman"
guess = ""
print("Who is bruce wayne..??")

while guess != secret_word:
    guess = input("Enter a guess: ")

print("You Won")