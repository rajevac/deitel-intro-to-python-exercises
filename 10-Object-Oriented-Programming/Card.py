class Card:
    FACE = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    SUIT = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, face):
        self._face = face

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        self._suit = suit

    def __repr__(self):
        return f'Card(face: {self.face}, suit = {self.suit}'

    def __str__(self):
        return f'{self.face} of {self.suit}'

    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'
