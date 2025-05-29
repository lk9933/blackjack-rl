from hand import Hand
from deck import Deck

class CardHolder:
    """Base class for any entity that holds cards."""

    def __init__(self):
        self.hand = Hand()

    def draw(self, deck: Deck) -> None:
        self.hand.add_card(deck.draw_card())

    def reset_hand(self) -> None:
        self.hand.clear()