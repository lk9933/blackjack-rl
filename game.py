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
            print("You cannot place a bet outside of the betting round.")
            return False
        try:
            self.player.place_bet(amount)
            self.current_bet = amount
            return self.start_round()
        except Exception as e:
            print(e)
            return False
        
    def start_round(self) -> bool:
        if self.game_state != GameState.BETTING or self.current_bet <= 0:
            print("Place a bet first.")
            return False
        
        self.player.reset_hand()
        self.dealer.reset_hand()

        for _ in range(2):
            self.player.draw(self.deck)
            self.player.draw(self.deck)

        player_hand_values = self.player.hand.get_values()

        if BLACKJACK_HAND_VALUE in player_hand_values:
            return self.handle_player_blackjack()
        
        self.game_state = GameState.PLAYER_TURN
        return True

    def handle_player_blackjack(self) -> bool:
        print("BLACKJACK")
        dealer_hand_values = self.dealer.hand.get_values()

        if BLACKJACK_HAND_VALUE in dealer_hand_values:
            print("Dealer also has blackjack. Push!")
            self.player.add_to_bankroll(self.current_bet)
        else:
            payout = self.current_bet * BLACKJACK_PAYOUT
            print(f"You win ${payout}.")
            self.player.add_to_bankroll(self.current_bet + payout)

        self.game_state = GameState.BETTING
        self.current_bet = 0.0
        return True
    
    def player_hit(self) -> bool:
        if self.game_state != GameState.PLAYER_TURN:
            print("It is not your turn.")
            return False

        self.player.draw(self.deck)

        if self.player.hand.is_bust():
            print(f"BUST!")
            self.game_state = GameState.BETTING
            self.current_bet = 0.0

        return True
    
    def player_stand(self) -> bool:
        if self.game_state != GameState.PLAYER_TURN:
            print("It is not your turn.")
            return False

        self.player.stand()

        self.game_state = GameState.DEALER_TURN
        return self.dealer_play()
    
    def player_double_down(self) -> bool:
        if self.game_state != GameState.PLAYER_TURN:
            print("It is not your turn.")
            return False
        
        if not self.player.can_afford_bet(self.current_bet):
            print("Insufficient funds to double down.")
            return False
        
        self.player.double_down()
        self.current_bet *= 2

        self.player.draw(self.deck)

        if self.player.hand.is_bust():
            print(f"BUST!")
            self.game_state = GameState.BETTING
            self.current_bet = 0.0
            return True
        
        self.game_state = GameState.DEALER_TURN
        return self.dealer_play()
    
    def dealer_play(self) -> bool:
        if self.game_state != GameState.DEALER_TURN:
            print("It is not the dealer's turn.")
            return False
        
        print(f"Dealer's hand: {self.dealer.hand}")
        
        if BLACKJACK_HAND_VALUE in self.dealer.hand.get_values:
            print("Dealer has blackjack!")
            self.game_state = GameState.BETTING
            self.current_bet = 0.0
            return True
        
        while min(self.dealer.hand.get_values) < DEALER_STAND_VALUE:
            self.dealer.draw(self.deck)
            print(f"Dealer draws: {self.dealer.hand.cards[-1]}")

        return self.determine_winner()
    
    def determine_winner(self) -> bool:
        dealer_value = max(self.dealer.hand.get_values())
        player_value = max(self.player.hand.get_values())

        print(f"Your hand: {player_value}. Dealer's hand: {dealer_value}")

        if self.dealer.hand.is_bust():
            print("Dealer busts! You win!")
            self.player.add_to_bankroll(self.current_bet * 2)
        elif dealer_value > player_value:
            print("Dealer wins!")
        elif dealer_value < player_value:
            print("You win!")
        else:
            print("Push! It's a tie.")
            self.player.add_to_bankroll(self.current_bet)

        self.game_state = GameState.BETTING
        self.current_bet = 0.0
        return True
    
    def get_game_state(self) -> dict:
        return {
            "player_bankroll": self.player.bankroll,
            "current_bet": self.current_bet,
            "player_hand": str(self.player.hand),
            "player_hand_value": self.player.hand.get_values()
        }