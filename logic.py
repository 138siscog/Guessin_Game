import random

def check_logic(guess,num):

    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print("You guessed it!")
        running =  False
