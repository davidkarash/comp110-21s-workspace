"""An exercise in remainders and boolean logic."""

__author__ = "730407523"

user_num: int = int(input("Enter an int: "))

if user_num % 2 == 0:
    if user_num % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if user_num % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")