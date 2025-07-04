"""
Game-related constants.
"""

SUITS = [
    "Hearts",
    "Spades",
    "Diamonds",
    "Clubs"
]

RANKS = {
    "Ace": [1, 11],
    "Two": [2],
    "Three": [3],
    "Four": [4],
    "Five": [5],
    "Six": [6],
    "Seven": [7],
    "Eight": [8],
    "Nine": [9],
    "Ten": [10],
    "Jack": [10],
    "Queen": [10],
    "King": [10]
}

BLACKJACK_HAND_VALUE = 21
DEALER_STAND_VALUE = 17
BLACKJACK_PAYOUT = 1.5
INITIAL_DEAL = 2