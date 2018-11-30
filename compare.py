import deck


def make_a_deck():
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    return deck_of_cards


def draw_a_card(deck_of_cards):
    player_cards = []
    for cards in range(5):
        player_cards.append(deck_of_cards.draw_a_card())
    return player_cards


def compare(card1, card2):
    return card1.compared_to(card2)
    

def main():
    deck_of_cards = make_a_deck()
    player1 = draw_a_card(deck_of_cards)
    player2 = draw_a_card(deck_of_cards)
    for x in range(5):
        com = compare(player1[x], player2[x])
        print("Player 1 drew a", player1[x])
        print("Player 2 drew a", player2[x])
        print(" ")
        if com == player1[x]:
            print("Player 1 wins!")
            print()
        elif com == player2[x]:
            print("Player 2 wins!")
            print()


main()
