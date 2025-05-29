import random
from card import SUITS, RANKS, Card

class Deck:
    """Class representing a deck(s) of playing cards."""

    def __init__(self, shoe_size: int = 1) -> None:
        self.shoe_size = shoe_size
        self.deck = self.create_deck()

    def create_deck(self) -> None:
        deck = []
        for _ in range(self.shoe_size):
            for suit in SUITS:
                for rank in RANKS.keys():
                    deck.append(Card(suit, rank))
        return deck
    
    def shuffle_cards(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck.pop()
    
    def get_size(self) -> int:
        return len(self.deck)
    