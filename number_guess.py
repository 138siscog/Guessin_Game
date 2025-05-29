#impoty random
import random 
from logic import check_logic


#Set a random number between 1 and 100 to guess
num = random.randint(1, 100)

print("Press enter to start the game")
input()  # Wait for the user to press enter

#game loop
running = True
while running:

#ask the user to guess a number
    guess = int(input("guess a number between 1 and 100:"))

    check_logic(guess,num)

    if guess == num:
        running = False

#once the number is guessed, print the number
print("The number was:", num)