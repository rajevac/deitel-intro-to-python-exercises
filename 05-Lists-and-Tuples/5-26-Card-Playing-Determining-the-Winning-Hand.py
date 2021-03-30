import random

enumerate_ranks = {'Deuce': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                   'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

enumerate_hand_categories = {'High Card': 1, 'One Pair': 2, 'Two Pair': 3, 'Three of a Kind': 4, 'Straight': 5,
                             'Flush': 6, 'Full House': 7, 'Four of a kind': 8, 'Straight Flush': 9}


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
    hand_1 = []
    hand_2 = []
    idx = 0
    while idx < 10:
        if idx % 2 == 0:
            hand_1.append(deck.pop(0))
        else:
            hand_2.append(deck.pop(0))

        idx += 1

    return hand_1, hand_2


def hand_count(hand):
    '''
    :param hand: tuple with cards dealt
    :return: dictionary with cards in the hand
    Loop through the list of cards in hand, count how many of the same rank
    there is in the hand and return dictionary with rank name and how many times
    each rank appears in the hand. In addition check if we have a Flush and return
    dictionary. For example Full House {'King: 3, 'Four': 2, 'Flush': False}
    '''

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
    '''
    :param ranks: dictionary with card in hand ranks
    :return: boolean
    For Flush in hand, sort card ranks and check if there is a
    'Straight Flush' return True
    '''

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


def sort_ranks(h1, h2):
    '''
    :param h1: dictionary with cards in the hand
    :param h2: dictionary with cards in the hand
    :return: list with sorted card ranks for Player 1 and Player 2 eg. [14, 10, 7, 5, 2]
    '''

    p1 = []
    p2 = []

    for key in h1.keys():
        if key != 'Flush':
            p1.append(enumerate_ranks[key])

    for key in h2.keys():
        if key != 'Flush':
            p2.append(enumerate_ranks[key])

    p1.sort(reverse=True)
    p2.sort(reverse=True)

    return p1, p2


def find_a_winner(p1, p2):
    '''
    :param p1: sorted list of card ranks
    :param p2: sorted list of card ranks
    :return: Poker winner as a string
    '''
    i = 0
    while i < len(p1):
        if p1[i] > p2[i]:
            return 'Player 1 wins'
        elif p1[i] < p2[i]:
            return 'Player 2 wins'
        elif i == len(p1) - 1:
            return 'Draw'
        i += 1


def find_a_winner_three_four(p1, p2, num):
    '''
    :param p1: sorted list of card ranks
    :param p2: sorted list of card ranks
    :param num: integer: 3 if 'Three of a Kind' or 'Full House', 4 if 'Four of a Kind'
    :return: Poker winner as a string
    '''
    pair_1 = 0
    pair_2 = 0

    for key, value in p1.items():
        if value == num:
            pair_1 = enumerate_ranks[key]

    for key, value in p2.items():
        if value == num:
            pair_2 = enumerate_ranks[key]

    if pair_1 > pair_2:
        return 'Player 1 wins'
    else:
        return 'Player 2 wins'


def who_has_higher_hand(player_1_hand, player_2_hand, hand_cat):
    '''
    :param player_1_hand: dictionary with cards in the hand
    :param player_2_hand: dictionary with cards in the hand
    :param hand_cat: hand category
    :return: Winner as string: Player 1 or Player 2 or Draw

    This function is called when players has the same hand category, for example
    both players have 'Three of a Kind' and we still have to determine who has the higher hand.
    '''

    if hand_cat == 'High Card':
        p1, p2 = sort_ranks(player_1_hand, player_2_hand)
        return find_a_winner(p1, p2)

    elif hand_cat == 'One Pair':

        pair_1 = 0
        pair_2 = 0

        for key, value in player_1_hand.items():
            if value == 2:
                pair_1 = enumerate_ranks[key]

        for key, value in player_2_hand.items():
            if value == 2:
                pair_2 = enumerate_ranks[key]

        if pair_1 > pair_2:
            return 'Player 1 wins'
        elif pair_1 < pair_2:
            return 'Player 2 wins'
        else:
            p1, p2 = sort_ranks(player_1_hand, player_2_hand)
            return find_a_winner(p1, p2)

    elif hand_cat == 'Two Pair':

        pair_1 = []
        pair_2 = []

        for key, value in player_1_hand.items():
            if value == 2:
                pair_1.append(enumerate_ranks[key])

        for key, value in player_2_hand.items():
            if value == 2:
                pair_2.append(enumerate_ranks[key])

        pair_1.sort(reverse=True)
        pair_2.sort(reverse=True)

        i = 0
        while i < len(pair_1):
            if pair_1[i] > pair_2[i]:
                return 'Player 1 wins'
            elif pair_1[i] < pair_2[i]:
                return 'Player 2 wins'

            i += 1

        p1, p2 = sort_ranks(player_1_hand, player_2_hand)
        return find_a_winner(p1, p2)

    elif hand_cat == 'Three of a Kind':
        return find_a_winner_three_four(player_1_hand, player_2_hand, 3)

    elif hand_cat == 'Straight':
        p1, p2 = sort_ranks(player_1_hand, player_2_hand)
        return find_a_winner(p1, p2)

    elif hand_cat == 'Flush':
        p1, p2 = sort_ranks(player_1_hand, player_2_hand)
        return find_a_winner(p1, p2)

    elif hand_cat == 'Full House':
        return find_a_winner_three_four(player_1_hand, player_2_hand, 3)

    elif hand_cat == 'Four of a Kind':
        return find_a_winner_three_four(player_1_hand, player_2_hand, 4)

    elif hand_cat == 'Straight Flush':
        p1, p2 = sort_ranks(player_1_hand, player_2_hand)
        return find_a_winner(p1, p2)


def hand_category(hand):
    '''
    :param hand: tuple with cards dealt
    :return: hand category as a string
    Dictionary length can be use to find hand category,
    except for 'Straight Flush' and 'Flush'
    '''

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

    return 'Something went wrong, evaluation is not correct'


# Deal cards, print card in hand, print hand category
player_1, player_2 = deal_cards(initialize_deck())

print(f'Player 1 cards: {player_1}')
print(f'Player 2 cards: {player_2}')
print('\n')
print(f'Player 1 hand category: {hand_category(player_1)}')
print(f'Player 2 hand category: {hand_category(player_2)}')
print('\n')

# Get hand category and find a winner
player_1_category = hand_category(player_1)
player_2_category = hand_category(player_2)

if player_1_category == player_2_category:
    winner = who_has_higher_hand(hand_count(player_1), hand_count(player_2), player_1_category)
    print(f'Winner: {winner}')
else:
    if enumerate_hand_categories[player_1_category] > enumerate_hand_categories[player_2_category]:
        print('Winner: Player 1 wins')
    else:
        print('Winner: Player 2 wins')

