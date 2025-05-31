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
        # Return any existing bet to bankroll first
        self.bankroll += self.bet
        self.bet = 0
        
        if bet <= 0:
            raise ValueError("Bet amount must be positive")
            
        if self.can_afford_bet(bet):
            self.bet = bet
            self.bankroll -= bet
        else:
            raise ValueError(f"Insufficient funds: ${self.bankroll} available, ${bet} required")

    def double_down(self) -> None:
        additional_bet = self.bet
        if additional_bet <= 0:
            raise ValueError("No active bet to double")
            
        if self.can_afford_bet(additional_bet):
            self.bankroll -= additional_bet
            self.bet += additional_bet  # More explicit than multiplying
        else:
            raise ValueError(f"Insufficient funds to double: ${self.bankroll} available, ${additional_bet} required")
        
    def add_to_bankroll(self, amount: float) -> None:
        self.bankroll += amount

    def can_afford_bet(self, bet: float) -> bool:
        return bet <= self.bankroll

    def stand(self) -> None:
        pass