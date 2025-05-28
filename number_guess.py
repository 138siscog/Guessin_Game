#impoty random
import random 

#Set a random number between 1 and 100 to guess
num = random.randint(1, 100)

#game loop
running = True
while running:
    #ask the user to guess a number
    guess = int(input("guess a number between 1 and 100:"))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print("You guessed it!")
        running = False
#once the number is guessed, print the number
print("The number was:", num)