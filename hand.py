from card import Card

class Hand:
    """Class representing a hand of playing cards."""
    
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def show_card(self, index: int) -> Card:
        if index > len(self.cards) - 1:
            raise IndexError("index outside range")
        return self.cards[index]

    def clear(self) -> None:
        self.cards = []

    def get_values(self) -> set:
        possible_values = {0}
        for card in self.cards:
            new_values = set()
            card_vals = card.get_value()
            for elem in possible_values:
                for val in card_vals:
                    new_values.add(elem + val)
            possible_values = new_values

        def validate_value(value: int) -> bool:
            return not value > 21
        
        return set(filter(validate_value, possible_values))
    
    def __str__(self) -> str:
        return "\n".join(str(card) for card in self.cards)

    
    