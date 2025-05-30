import sys
from game import BlackjackGame

def print_help():
    """Print available commands."""
    print("\nAvailable commands:")
    print("  bet <amount> - Place a bet")
    print("  hit         - Take another card")
    print("  stand       - End your turn")
    print("  double      - Double your bet and take one more card")
    print("  status      - Show game status")
    print("  help        - Show this help")
    print("  quit        - Exit the game\n")

def main():
    """Main function to run the Blackjack game."""
    print("Welcome to Blackjack!")
    
    # Get starting bankroll from the player
    try:
        bankroll = float(input("Enter your starting bankroll: $"))
        if bankroll <= 0:
            print("Bankroll must be greater than 0. Using default $1000.")
            bankroll = 1000
    except ValueError:
        print("Invalid input. Using default $1000.")
        bankroll = 1000
    
    # Initialize the game
    game = BlackjackGame(bankroll=bankroll)
    
    print_help()
    
    # Main game loop
    while True:
        state = game.get_game_state()
        print(f"\nBankroll: ${state['player_bankroll']:.2f}")
        
        if game.game_state.value == "betting":
            print("--- Betting Phase ---")
            command = input("Enter command (bet/status/help/quit): ").strip().lower()
        else:
            print(f"--- {game.game_state.value.capitalize()} ---")
            print(f"Your hand: {state['player_hand']} (Value: {max(state['player_hand_value'])})")
            print(f"Current bet: ${game.current_bet:.2f}")
            command = input("Enter command: ").strip().lower()
        
        if command.startswith("bet "):
            try:
                amount = float(command.split()[1])
                if game.place_bet(amount):
                    print(f"Bet placed: ${amount:.2f}")
                    game.start_round()
            except (ValueError, IndexError):
                print("Invalid bet amount.")
        
        elif command == "hit":
            if game.player_hit():
                print(f"New hand: {game.player.hand}")
        
        elif command == "stand":
            game.player_stand()
            
        elif command == "double":
            if game.player_double_down():
                print(f"Bet doubled to ${game.current_bet:.2f}")
                print(f"New hand: {game.player.hand}")
            
        elif command == "status":
            print(f"Game state: {game.game_state.value}")
            print(f"Your bankroll: ${state['player_bankroll']:.2f}")
            print(f"Current bet: ${game.current_bet:.2f}")
            print(f"Your hand: {state['player_hand']}")
            if game.dealer.hand.cards:
                if game.game_state.value == "dealer's turn" or game.game_state.value == "game over":
                    print(f"Dealer's hand: {game.dealer.hand}")
                else:
                    # Show only the first card if it's still player's turn
                    print(f"Dealer's up card: {game.dealer.show_first_card()}")
            
        elif command == "help":
            print_help()
            
        elif command == "quit":
            print(f"Thanks for playing! You're leaving with ${state['player_bankroll']:.2f}")
            sys.exit(0)
            
        else:
            print("Invalid command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()