from card import Card

class Hand:
    """Class representing a hand of playing cards."""
    
    def __init__(self) -> None:
        self.cards = []
        self.values = set()

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self._recalculate_values()

    def _recalculate_values(self) -> None:
        self.values = {0}
        for card in self.cards:
            card_values = card.get_value()
            self.values = {v + cv for v in self.values for cv in card_values}
        self.values = {val for val in self.values if val <= 21}

    def show_card(self, index: int) -> Card:
        if index < 0 or index >= len(self.cards):
            raise IndexError("index outside range")
        return self.cards[index]

    def clear(self) -> None:
        self.cards = []
        self.values = set()

    def get_values(self) -> set:
        return self.values
    
    def is_bust(self) -> bool:
        return len(self.values) == 0 or max(self.values) <= 0
        
    def __str__(self) -> str:
        return "\n".join(str(card) for card in self.cards)

    
    