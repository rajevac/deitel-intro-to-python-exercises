import random


def initialize_deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))

    random.shuffle(deck)

    return deck


cards = initialize_deck()


for idx in range(0, 52, 4):
    card_1 = f'{cards[idx][0]} of {cards[idx][1]}'
    card_2 = f'{cards[idx+1][0]} of {cards[idx+1][1]}'
    card_3 = f'{cards[idx+2][0]} of {cards[idx+2][1]}'
    card_4 = f'{cards[idx+3][0]} of {cards[idx+3][1]}'
    print(f'{card_1:<25}{card_2:<25}{card_3:<25}{card_4:<25}')