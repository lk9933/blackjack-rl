from card import Card
from hand import Hand
from deck import Deck

def main():
    # ace_of_spades = Card("Spades", "Ace")
    # ace_of_hearts = Card("Hearts", "Ace")
    # jack_of_spades = Card("Spades", "Jack")
    # card_list = [ace_of_hearts, ace_of_spades, jack_of_spades]
    # test_hand = Hand(card_list)
    # for val in test_hand.get_values():
    #     print(val)
    test_deck = Deck(1)
    test_deck.shuffle_cards()
    test_hand_cards = []
    test_hand_cards.append(test_deck.draw_card())
    test_hand_cards.append(test_deck.draw_card())
    test_hand = Hand(test_hand_cards)
    print(test_hand)
    print(" ".join(str(val) for val in test_hand.get_values()))

if __name__=="__main__":
    main()
