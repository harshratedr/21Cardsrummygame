"""21 Card Rummy game"""

__author__ = "Harsh Nagwanshi"
__copyright__ = "Copyright 2024, The Black-Myth Project"
__credits__ = ["Hustle"]
__version__ = "1.1.0"
__maintainer__ = "Harsh Nagwanshi"
__email__ = "harshnagwanshi.trs@gmail.com"
__status__ = "Productive"


#Custurd of Codes start here

import random


suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

def get_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def hand_value(hand):
    value = sum(ranks[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(name, hand):
    print(f"{name}'s hand: {', '.join(f'{rank} of {suit}' for rank, suit in hand)} (Value: {hand_value(hand)})")

def game_logic():
    print("Welcome to 21-Card Rummy game")
    chip_pool = int(input("Enter buy-in amount: "))
    
    while True:
        if chip_pool <= 0:
            print("You have no chips left! Game over.")
            break
        
        bet = 0
        while bet <= 0 or bet > chip_pool:
            try:
                bet = int(input(f"You have {chip_pool} chips. Enter bet amount: "))
                if bet > chip_pool:
                    print("You cannot bet more than you have!")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        deck = get_deck()
        random.shuffle(deck)
        
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        
        display_hand("Player", player_hand)
        display_hand("Dealer", dealer_hand)
        
        while True:
            if hand_value(player_hand) > 21:
                print("Bust! You lose.")
                chip_pool -= bet
                break
            move = input("Hit (h) or Stand (s)? ").lower()
            if move == 'h':
                player_hand.append(deal_card(deck))
                display_hand("Player", player_hand)
            elif move == 's':
                break
        
        if hand_value(player_hand) <= 21:
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card(deck))
            
            display_hand("Dealer", dealer_hand)
            player_score = hand_value(player_hand)
            dealer_score = hand_value(dealer_hand)
            
            if dealer_score > 21 or player_score > dealer_score:
                print("You win!")
                chip_pool += bet
            elif player_score < dealer_score:
                print("Dealer wins!")
                chip_pool -= bet
            else:
                print("It's a tie!")
        
        print(f"Chip Total: {chip_pool}")
        
        restart = input("Play again? (y/n): ").lower()
        if restart != 'y':
            print("Thanks for playing!")
            break

game_logic()
