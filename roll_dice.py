"""
The program consists of asking the user if he wants to roll the dice,
depending on the assigned parameters, he will print a number in that range
"""
import random

def rolldice(min,max):
    # ask the user
    ask_the_user=input("do you want to play roll the dice(yes/y or no/n)?: ")
    # validation
    while ask_the_user=="yes" or ask_the_user=="y":
        # Logic
        print("rolling the dice...")
        number=random.randint(min,max)
        print("your number is", number)
        # ask the user
        ask_the_user=input("roll the dice again(yes/y or no/n)?: ")
    else:
        print("no problem")
# function call
rolldice(1,6)
        

