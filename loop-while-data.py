"""
Use a while loop
Use a for loop

"""

import random

# print("Working with a while loop")
# print("A while loop makes a section of code repeat until a certain condition is met. \nIn this exercise, you will create a Python script that asks the user to correctly guess a number.")
# print("\n")
# print("Welcome to Guess the Number!")
# print("The rules are simple. I will think of a number, and you will try to guess it.")
# number = random.randint(1,10)
# isGuessRight = False
# while isGuessRight != True:
#     guess = input("Guess a number between 1 and 10: ")
#     if int(guess) == number:
#         print("You guessed {}. That is correct! You win!".format(guess))
#         isGuessRight = True
#     else:
#         print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

print("Writing pseudocode")
number = random.randint(1,10)
isGuessRight = False
#If the user has not guessed the correct answer, enter the loop.
while isGuessRight != True:
    #Ask the user for a guess
    guess = input("Guess a number between 1 and 10: ")
    #Is the guess the correct number?
    if int(guess) == number:
        #If the correct guess, tell the user it was the correct guess and exit the loop.
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        #If the wrong guess, tell the user it was the wrong guess and continue the loop.
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
