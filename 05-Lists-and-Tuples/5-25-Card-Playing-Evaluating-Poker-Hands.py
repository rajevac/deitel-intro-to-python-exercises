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


def deal_cards(deck):
    hand = []
    idx = 0
    while idx < 5:
        hand.append(deck.pop(0))
        idx += 1
    return hand


enumerate_ranks = {'Deuce': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                   'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Might be handy for solving 5.26 problem
# enumerate_hand_categories = {'High Card': 1, 'One Pair': 2, 'Two Pair': 3, 'Three of a kind': 4, 'Straight': 5,
#                             'Flush': 6, 'Full House': 7, 'Four of a kind': 8, 'Straight Flush': 9}


def hand_count(hand):
    # count suits (is there a flash in a hand)
    # count how many times each rank is in the hand (eg. 'Deuce': 1, 'King': 2)
    # return hand dictionary
    ranks = []
    suits = []
    count_ranks_and_suits = {}

    for i in range(len(hand)):
        ranks.append(hand[i][0])
        suits.append(hand[i][1])

    for i in range(len(ranks)):
        if ranks[i] not in count_ranks_and_suits.keys():
            count_ranks_and_suits[ranks[i]] = ranks.count(ranks[i])

    count_suits = suits.count(suits[0])
    if count_suits == 5:
        count_ranks_and_suits['Flush'] = True
    else:
        count_ranks_and_suits['Flush'] = False

    return count_ranks_and_suits


def is_straight(ranks):

    ranks_as_integers = []

    for key in ranks.keys():
        if key != 'Flush':
            ranks_as_integers.append(enumerate_ranks[key])

    ranks_as_integers.sort()

    for i in range(len(ranks_as_integers) - 1):

        if ranks_as_integers[i] == ranks_as_integers[i + 1] - 1:
            continue
        else:
            return False

    return True


def hand_category(hand):

    hand_value = hand_count(hand)

    if hand_value['Flush']:

        if is_straight(hand_value):
            return 'Straight Flush'
        else:
            return 'Flush'

    elif len(hand_value) == 6:

        if is_straight(hand_value):
            return 'Straight'
        else:
            return 'High Card'

    elif len(hand_value) == 5:
        return 'One Pair'

    elif len(hand_value) == 4:

        for value in hand_value.values():
            if value == 3:
                return 'Three of a Kind'
        return 'Two Pair'

    elif len(hand_value) == 3:

        for value in hand_value.values():
            if value == 4:
                return 'Four of a Kind'
        return 'Full House'

    return 'Still figuring out'

hand_1 = deal_cards(initialize_deck())

print(hand_1)
print(hand_category(hand_1))

