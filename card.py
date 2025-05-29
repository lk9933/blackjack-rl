from constants import RANKS, SUITS

class Card:
    """Class representing a playing card with a rank and a suit."""

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def get_value(self) -> list[int]:
        return RANKS[self.rank]
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
