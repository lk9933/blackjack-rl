from card import Card
from hand import Hand
from deck import Deck
from config import CONFIG

class Game:
    def __init__(self) -> None:
        self.deck = Deck(CONFIG["shoe_size"])
        self.player_hands = []
        self.dealer_hand = None
        self.initial_deal()
        self.current_bet = 0
        self.game_over = False
        self.winner = None

    def initial_deal(self):
        player_hand = Hand()
        dealer_hand = Hand()

        for _ in range(2):
            player_hand.add_card(self.deck.draw_card())
            dealer_hand.add_card(self.deck.draw_card())

        self.player_hands.append(player_hand)
        self.dealer_hand = dealer_hand
    
    def reset_round(self):
        self.player_hands = []
        