"""21 Cards Rummy game"""


__author__ = "Harsh Nagwanshi"
__copyright__ = "Copyright 2024, The Black Myth Project"
__credits__ = ["Hustle"]
__version__ = "1.1.0"
__maintainer__ = "Harsh Nagwanshi"
__email__ = "harshnagwanshi.trs@gmail.com"
__status__ = "Productive"


#Code start

import random

# Card deck setup
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

def blackjack_game():
    print("Welcome to Blackjack!")
    deck = get_deck()
    random.shuffle(deck)
    
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    while True:
        display_hand("Player", player_hand)
        if hand_value(player_hand) > 21:
            print("Bust! You lose.")
            return
        move = input("Hit (h) or Stand (s)? ").lower()
        if move == 'h':
            player_hand.append(deal_card(deck))
        elif move == 's':
            break
    
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    
    display_hand("Dealer", dealer_hand)
    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)
    
    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

blackjack_game()
