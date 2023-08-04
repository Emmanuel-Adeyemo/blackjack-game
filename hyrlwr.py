
import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)

def game():
    """ higher or lower game """
    
    first_item = random.choice(data)
   
    second_item = random.choice(data)
        
    def show_instructions(first, second):
           
        print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.")
        
        print(vs)
        
        print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}.")
    
        
    
    def check_answer(guess, first, second):
        """ checks if guess is higher or lower """
       
        first_followers = first["follower_count"]
        
        second_followers = second["follower_count"]
    
        max_value = max(first_followers, second_followers) # check max value
     
        if guess == "a":
            guess_value = first_followers
    
        else:
            guess_value = second_followers
    
        if guess_value != max_value:
            user_continue = False
            return user_continue
    
        else:
            
            user_continue = True
            return user_continue
                      
        
        
    user_is_correct = True
    score = 0
    
    while user_is_correct:
    
        show_instructions(first_item, second_item)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        check = check_answer(guess, first_item, second_item)
        if check is False:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        else:
       
            first_item = second_item
            second_item = random.choice(data)
            clear()
            print(logo)
            score += 1
            print(f"You're right! Current score: {score}")



game()
