import random
from card import Card
from constants import SUITS, RANKS

class Deck:
    """Class representing a deck(s) of playing cards."""

    def __init__(self, shoe_size: int = 1) -> None:
        self.shoe_size = shoe_size
        self.deck = []
        self.create_deck()
        self.shuffle_cards()  # Always shuffle a new deck

    def create_deck(self) -> None:
        self.deck = []
        for _ in range(self.shoe_size):
            for suit in SUITS:
                for rank in RANKS.keys():
                    self.deck.append(Card(suit, rank))
    
    def shuffle_cards(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck.pop()
    
    def get_size(self) -> int:
        return len(self.deck)
    
    def reset_deck(self) -> None:
        self.create_deck()
        self.shuffle_cards()
    