from Card import Card
import random


class DeckOfCards:
    NUMBER_OF_CARDS = 52

    def __init__(self):
        self._deck = []
        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACE[count % 13], Card.SUIT[count // 13]))

    def shuffle(self):
        return random.shuffle(self._deck)

    def deal_card(self):
        try:
            card = self._deck.pop(0)
            return card
        except LookupError:
            return None

    def __str__(self):
        s = ''
        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<25}'
            if (index+1) % 4 == 0:
                s += '\n'
        return s
