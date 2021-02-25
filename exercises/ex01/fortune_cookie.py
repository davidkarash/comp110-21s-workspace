"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730407523"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")

magic_number: int = randint(1, 100)

if magic_number > 50:
    if magic_number > 75:
        print("This will surely be a magical day for you!")
    else:
        print("Tomorrow, a great change will happen in your life that you may not have been expecting.")
else:
    if magic_number > 25:
        print("Make the most of your day today, and good things will come.")
    else:
        print("What you have been looking for will soon be realized in your life!")

print("Now, go spread positive vibes!")