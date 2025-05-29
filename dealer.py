from player import Player
from hand import Hand
from deck import Deck
from card import Card
from cardholder import CardHolder

class Dealer(CardHolder):
    """Class representing the dealer in a game of Blackjack."""

    def __init__(self):
        super().__init__()

    def show_first_card(self) -> Card:
        self.hand.show_card(0)