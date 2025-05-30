from hand import Hand
from deck import Deck
from cardholder import CardHolder

class Player(CardHolder):
    """Class representing a player in a game of Blackjack"""

    def __init__(self, bankroll: float, bet: float = 0):
        super().__init__()
        self.bankroll = bankroll
        self.bet = bet

    def place_bet(self, bet: float) -> None:
        self.bankroll += self.bet
        if self.can_afford_bet(bet):
            self.bet = bet
            self.bankroll -= bet
        else:
            raise Exception("cannot afford bet")

    def double_down(self) -> None:
        additional_bet = self.bet
        if self.can_afford_bet(additional_bet):
            self.bankroll -= additional_bet
            self.bet *= 2
        else:
            raise Exception("cannot afford bet")
        
    def add_to_bankroll(self, amount: float) -> None:
        self.bankroll += amount

    def can_afford_bet(self, bet: float) -> bool:
        return bet <= self.bankroll

    def stand(self) -> None:
        pass