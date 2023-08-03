import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def game():
    """ The Number Guessing Game """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    
    level = input("Choose your level of difficulty. Type 'easy' or 'hard': ")
    
    if level == "easy":
        lives = EASY_LEVEL
        print(f"You have {lives} attempts remaining to guess the number.")
    elif level == "hard":
        lives = HARD_LEVEL
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        print(f"{level} is invalid")
        # to break the loop
        lives = 0
    
    number = random.randint(1, 100)
    
    guess = 0
    
    def number_check():
        
        """ Compares the guess to the random number"""
    
        if guess > number and lives - 1 != 0:
            print("Too high.\nGuess again.")
            print(f"You have {lives - 1} attempts remaining to guess the number.")
            return lives - 1
            
            
        elif guess < number and lives - 1 != 0:
            print("Too low.\nGuess again.")
            print(f"You have {lives - 1} attempts remaining to guess the number.")
            return lives - 1
            
        
        elif guess == number:
            print(f"You got it! The number was {number}.")
            return lives

        elif lives - 1 == 0 and guess > number:
            print("Too high")
            print("You've run out of guesses, you lose.")
            return lives - 1

        elif lives - 1 == 0 and guess < number:
            print("Too low")
            print("You've run out of guesses, you lose.")
            return lives - 1
            
            
        
    #check guessed number and provide feedback
    
    while lives > 0 and guess != number:
            
        guess = int(input("Make a guess: "))
        
        lives = number_check()
        # if lives == 0:
        #     print("You've run out of guesses, you lose.")


 
game()
