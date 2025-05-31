from deck import Deck
from player import Player
from dealer import Dealer
from constants import BLACKJACK_HAND_VALUE, BLACKJACK_PAYOUT, DEALER_STAND_VALUE, INITIAL_DEAL
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
        if amount <= 0:
            print("Bet amount must be greater than zero.")
            return False
        try:
            self.player.place_bet(amount)
            self.current_bet = amount
            # Don't automatically start the round, just return success
            return True
        except Exception as e:
            print(e)
            return False
        
    def start_round(self) -> bool:
        if self.game_state != GameState.BETTING or self.current_bet <= 0:
            print("Place a bet first.")
            return False
        
        self.player.reset_hand()
        self.dealer.reset_hand()

        for _ in range(INITIAL_DEAL):
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)

        player_hand_values = self.player.hand.get_values()
        dealer_hand_values = self.dealer.hand.get_values()

        if BLACKJACK_HAND_VALUE in dealer_hand_values:
            if BLACKJACK_HAND_VALUE in player_hand_values:
                print("Both you and the dealer have blackjack. Push!")
                self.player.add_to_bankroll(self.current_bet)
            else:
                print("Dealer has blackjack!")
            self.game_state = GameState.BETTING
            self.current_bet = 0.0
            return True

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
            print(f"Insufficient funds to double down. You need ${self.current_bet:.2f} more.")
            return False
        
        try:
            self.player.double_down()
            self.current_bet *= 2
            
            # Draw card after doubling bet
            self.player.draw(self.deck)
            
            if self.player.hand.is_bust():
                print(f"BUST!")
                self.game_state = GameState.BETTING
                self.current_bet = 0.0
                return True
            
            # After double down, player's turn ends automatically
            self.game_state = GameState.DEALER_TURN
            return self.dealer_play()
        except ValueError as e:
            print(e)
            return False
    
    def dealer_play(self) -> bool:
        if self.game_state != GameState.DEALER_TURN:
            print("It is not the dealer's turn.")
            return False
        
        print(f"Dealer's hand: {self.dealer.hand}")
        
        if BLACKJACK_HAND_VALUE in self.dealer.hand.get_values():
            print("Dealer has blackjack!")
            self.game_state = GameState.BETTING
            self.current_bet = 0.0
            return True
        
        dealer_values = self.dealer.hand.get_values()
        while dealer_values and min(dealer_values) < DEALER_STAND_VALUE:
            self.dealer.draw(self.deck)
            print(f"Dealer draws: {self.dealer.hand.cards[-1]}")
            dealer_values = self.dealer.hand.get_values()
            if not dealer_values:  # Dealer busted
                break

        return self.determine_winner()
    
    def determine_winner(self) -> bool:
        dealer_values = self.dealer.hand.get_values()
        player_values = self.player.hand.get_values()
        
        if not dealer_values:  # Dealer busted
            print("Dealer busts! You win!")
            # Return original bet plus winnings
            self.player.add_to_bankroll(self.current_bet * 2)
        elif not player_values:  # Player busted (this shouldn't happen here but for completeness)
            print("You've busted!")
            # No need to adjust bankroll, bet was already taken
        else:
            dealer_value = max(dealer_values)
            player_value = max(player_values)
            
            print(f"Your hand: {player_value}. Dealer's hand: {dealer_value}")
            
            if dealer_value > player_value:
                print("Dealer wins!")
                # No need to adjust bankroll, bet was already taken
            elif dealer_value < player_value:
                print("You win!")
                # Return original bet plus winnings
                self.player.add_to_bankroll(self.current_bet * 2)
            else:
                print("Push! It's a tie.")
                # Return just the original bet
                self.player.add_to_bankroll(self.current_bet)

        # Reset for the next round
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