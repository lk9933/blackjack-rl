from hand import Hand
from deck import Deck
from cardholder import CardHolder

class Player(CardHolder):
    """Class representing a player in a game of Blackjack"""

    def __init__(self, bet: float, bankroll: float):
        super().__init__()
        self.bet = bet
        self.bankroll = bankroll

    def place_bet(self, bet: float) -> None:
        if self.can_afford_bet(bet):
            self.bet = bet
            self.bankroll -= bet
        else:
            raise Exception("Cannot afford bet")

    def double_down(self) -> None:
        double_bet = self.bet * 2
        if self.can_afford_bet(double_bet):
            self.bankroll -= self.bet
            self.bet = double_bet
        else:
            raise Exception("Cannot afford bet")

    def can_afford_bet(self, bet: float) -> bool:
        return bet < self.bankroll

    def stand(self) -> None:
        pass