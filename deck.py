import random
from card import Card
from constants import SUITS, RANKS

class Deck:
    def __init__(self, shoe_size: int = 1) -> None:
        self.shoe_size = shoe_size
        self.cards = self.create_deck()

    def create_deck(self) -> None:
        cards = []
        for _ in range(self.shoe_size):
            for suit in SUITS:
                for rank in RANKS.keys():
                    cards.append(Card(suit, rank))
        return cards
    
    def shuffle_cards(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()
    