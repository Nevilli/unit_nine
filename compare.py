# Liam Neville
# 12/3/18
# This program allows the user to run a game of compare (quaker version of war) between two players.


import deck


def make_a_deck():
    """
    This function creates a shuffled deck of 52 cards
    :return: deck_of_cards is returned to be used later on in order to draw the cards
    """
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    return deck_of_cards


def draw_a_card(deck_of_cards):
    """
    This function draws 5 cards for the 2 players
    :param deck_of_cards: This is the shuffled deck of 52 cards
    :return: player_cards is returned to be compared later on in the game
    """
    player_cards = []
    for cards in range(5):
        player_cards.append(deck_of_cards.draw_a_card())
    return player_cards


def compare(card1, card2):
    """
    This function compares the players cards and selects the highest card
    :param card1: A random card from player 1
    :param card2: A random card from player 2
    :return: The winning card from the compare is returned
    """
    return card1.compared_to(card2)
    

def main():
    p1_score = 0
    p2_score = 0
    deck_of_cards = make_a_deck()
    player1 = draw_a_card(deck_of_cards)
    player2 = draw_a_card(deck_of_cards)
    for x in range(5):
        high_card = compare(player1[x], player2[x])
        print("Player 1 drew a", player1[x])
        print("Player 2 drew a", player2[x])
        print(" ")
        if high_card == player1[x]:
            p1_score += 1
            print("Player 1 wins this round!")
            print()
        elif high_card == player2[x]:
            p2_score += 1
            print("Player 2 wins this round!")
            print()
    if p1_score > p2_score:
        print("Player 1 wins the game!!!")
    else:
        print("Player 2 wins the game!!!")


main()
