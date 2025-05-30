from card import Card

class Hand:
    """Class representing a hand of playing cards."""
    
    def __init__(self) -> None:
        self.cards = []
        self.values = {0}

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        new_values = set()
        card_values = card.get_value()
        if not self.values:
            new_values = card_values
        else:
            for existing_value in self.values:
                for card_value in card_values:
                    new_values.add(existing_value + card_value)
        self.values = {val for val in new_values if 0 < val <= 21}

    def show_card(self, index: int) -> Card:
        if index < 0 or index >= len(self.cards):
            raise IndexError("index outside range")
        return self.cards[index]

    def clear(self) -> None:
        self.cards = []
        self.values = {}

    def get_values(self) -> set:
        return self.values
    
    def is_bust(self) -> bool:
        busted = True
        for value in self.values:
            if value <= 21 and value > 0:
                busted = False
                break
        return busted
        
    def __str__(self) -> str:
        return "\n".join(str(card) for card in self.cards)

    
    