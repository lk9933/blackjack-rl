from deck import Deck
from player import Player
from dealer import Dealer
from constants import BLACKJACK_HAND_VALUE, BLACKJACK_PAYOUT, DEALER_STAND_VALUE
from enum import Enum

class GameState(Enum):
    """Enumerated types representing the game state."""
    BETTING = "betting"
    PLAYER_TURN = "player's turn"
    DEALER_TURN = "dealer's turn"
    GAME_OVER = "game over"

class BlackjackGame:
    """Manages the state and flow of a Blackjack game."""

    def __init__(self, bankroll: float, num_decks: int = 6):
        self.deck = Deck(num_decks)
        self.player = Player(bankroll)
        self.dealer = Dealer()
        self.current_bet = 0.0
        self.game_state = GameState.BETTING

    def place_bet(self, amount: float) -> bool:
        if self.game_state != GameState.BETTING:
            print("cannot place bet outside of betting round")
            return False
        try:
            self.player.place_bet(amount)
            self.current_bet = amount
        except Exception as e:
            print(e)
            return False
        
    def start_round(self) -> bool:
        if self.game_state != GameState.BETTING or self.current_bet <= 0:
            print("place a bet first")
            return False
        
        self.player.reset_hand()
        self.dealer.reset_hand()

        for _ in range(2):
            self.player.draw(self.deck)
            self.player.draw(self.deck)

        if BLACKJACK_HAND_VALUE in self.player.hand.get_values():
            return self.handle_player_blackjack()
        
        
