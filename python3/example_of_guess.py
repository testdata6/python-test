#!/usr/bin/python

## example for game program


secret_word = "batman"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guess = False
print("You have only 3 Guess..\n")
print("Who is bruce wayne..??")

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guess = True
        break

if out_of_guess:
    print("Out of guesses")
else:
    print("You win")

#---------------------- OR
## example for game program


secret_word = "batman"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guess = False
print("You have only 3 Guess..\n")
print("Who is bruce wayne..??")

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses")
else:
    print("You win")