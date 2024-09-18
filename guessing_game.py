'''Py Guessing Game

1. Create a random number
2. User input a number
3. check if number is equal to random num

  - Higher? print "too high"
  - Lower? print "too low"
  - Right? print "Congratulations"

'''
import random

def guess(num):
    random_number = random.randint(1, num)
    user_guess = 0
    no_of_guesses = 1
    while user_guess != random_number:
        user_guess = int(input(f"Guess a number between a and {num}: "))
        if user_guess > random_number:
            print("Too high. Guess again")
            no_of_guesses += 1
        elif user_guess < random_number:
            print("Too Low. Guess again.")
            no_of_guesses += 1
    print(f"Congratulations. The number was indeed {random_number}. You had {no_of_guesses} guesses.")

guess(10)
