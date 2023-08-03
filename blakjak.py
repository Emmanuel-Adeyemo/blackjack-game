############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    
    deal = random.choice(cards)
    return deal


def calculate_score(card_type):
    
    #computer_score = sum(computer_cards)    
    blackjack = 11 in card_type and 10 in card_type
    #user_blackjack = 11 in user_cards and 10 in user_cards
    #if type == "computer":
    if blackjack and len(card_type) == 2:
        score = 0
        return score
    elif blackjack and len(card_type) > 2:
        score = sum(card_type)
        #return score
        if score > 21:
            if 11 in card_type:
                card_type.remove(11)
                card_type.append(1)
                score = sum(card_type)
                return score
            else:
                return score
        else:
            return score
    else:
        score = sum(card_type)
        return score

def first_compare(computer_score, user_score):
    if computer_score == 0:    
        print("Your opponent has blackjack. You lose " + '\U0001F928')
        bjack = True
        return bjack
        
    elif computer_score != 0 and user_score == 0:    
        print("You got a blackjack, you win " + '\U0001F603')
        bjack = True
        return bjack


def compare(computer_score, user_score):
    if user_score > 21:
        print("You went over. You lose " + '\U0001F928')
    elif user_score < 18:
        print("You lose " + '\U0001F928')
    elif user_score == 21 and computer_score != 21:
        print("You got a perfect score. You win " + '\U0001F603')
    elif user_score != 21 and computer_score == 21:
        print("Opponent got a perfect score. You lose " + '\U0001F928')
    elif user_score > computer_score:
        print("You went over the opponent's. You lose " + '\U0001F928')
    elif user_score < computer_score:
        print("Opponent went over. You win " + '\U0001F603')
    elif user_score == computer_score:
        print("It's a bust. You draw " + '\U0001F643')


check_continue = True
start = "y"

while check_continue: 
    if start == "n":
        break
    blackjack = False
    while not blackjack:
        start = input("Do you want to play a game of blackjack. Type 'y' or 'n': ")
        if start == "n":
            break
        else:        
            clear()
            print(logo)
            user_cards = []
            computer_cards = []
            
            user_cards.append(deal_card())
            user_cards.append(deal_card())
            
            computer_cards.append(deal_card())
            computer_cards.append(deal_card())
            
            computer_first_card = computer_cards[0]
            user_score = sum(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {computer_first_card}")
            
            
            computer_score = calculate_score(computer_cards)
            user_score = calculate_score(user_cards)
            
            bjack_res = first_compare(computer_score, user_score)
        if bjack_res is True:
            blackjack = True
        else:
          
            more_cards = "y"
            while user_score < 21 and more_cards == "y":        
                            
                # ask if user wants a new card
                more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
                if more_cards == "y":
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                    print(f"    Your cards: {user_cards}, current score: {user_score}")
                    print(f"    Computer's first card: {computer_first_card}")
                    
                elif more_cards == "n":
                    pass
                
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = sum(computer_cards)


            print(f"    Your final hand: {user_cards}, final score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            compare(computer_score, user_score)
            
    check_continue = True        
    
    
    
