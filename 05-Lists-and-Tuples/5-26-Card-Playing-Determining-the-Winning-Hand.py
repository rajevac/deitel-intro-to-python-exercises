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


enumerate_ranks = {'Deuce': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                   'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

enumerate_hand_categories = {'High Card': 1, 'One Pair': 2, 'Two Pair': 3, 'Three of a Kind': 4, 'Straight': 5,
                             'Flush': 6, 'Full House': 7, 'Four of a kind': 8, 'Straight Flush': 9}


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


def sort_ranks(h1, h2):
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


def who_has_higher_hand(player_1_hand, player_2_hand, hand_rank):

    if hand_rank == 'High Card':
        # sort hands in list and compare last list items
        # if they are the same print draw
        # if player 1 > player 2 print player 1 wins else player 2 wins

        p1, p2 = sort_ranks(player_1_hand, player_2_hand)

        i = 0
        while i < len(p1):
            if p1[i] > p2[i]:
                return 'Player 1 wins'
            elif p1[i] < p2[i]:
                return 'Player 2 wins'
            elif i == len(p1) - 1:
                return 'Draw'
            i += 1

    elif hand_rank == 'One Pair':
        # get a key with value 2
        # grater key wins
        # if the same sort all key values
        # compare -1 value if the same move to -2 and so on
        # until you find the grates value
        # if not print draw

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

            i = 0
            print(len(p1))
            while i < len(p1):
                if p1[i] > p2[i]:
                    return 'Player 1 wins'
                elif p1[i] < p2[i]:
                    return 'Player 2 wins'
                elif i == len(p1) - 1:
                    return 'Draw'
                i += 1

    elif hand_rank == 'Two Pair':
        # get a key with value 2 and put them in the sorted list
        # compare key -1
        # grater key wins
        # if the same compare key -2
        # grater key wins
        # if the same compare key 0
        # grater key wins
        # if the same print draw
        pair_1 = []
        pair_2 = []

        for key, value in player_1_hand.items():
            if value == 2:
                pair_1.append(enumerate_ranks[key])

        for key, value in player_2_hand.items():
            if value == 2:
                pair_2.append(enumerate_ranks[key])

        pair_1.sort()
        pair_2.sort()

        i = 0
        while i < len(pair_1):
            if pair_1[i] > pair_2[i]:
                return 'Player 1 wins'
            elif pair_1[i] < pair_2[i]:
                return 'Player 2 wins'

            i += 1

        p1, p2 = sort_ranks(player_1_hand, player_2_hand)

        i = 0
        while i < len(p1):
            if p1[i] > p2[i]:
                return 'Player 1 wins'
            elif p1[i] < p2[i]:
                return 'Player 2 wins'
            elif i == len(p1) - 1:
                return 'Draw'
            i += 1

    elif hand_rank == 'Three of a Kind':
        # get keys with value 3
        # if player 1 > player 2 print player 1 wins else player 2 wins
        pair_1 = 0
        pair_2 = 0

        for key, value in player_1_hand.items():
            if value == 3:
                pair_1 = enumerate_ranks[key]

        for key, value in player_2_hand.items():
            if value == 3:
                pair_2 = enumerate_ranks[key]

        if pair_1 > pair_2:
            return 'Player 1 wins'
        else:
            return 'Player 2 wins'

    elif hand_rank == 'Straight':
        # SAME AS HIGH CARD
        # sort hands in list and compare last list items
        # if they are the same print draw
        # if player 1 > player 2 print player 1 wins else player 2 wins
        p1, p2 = sort_ranks(player_1_hand, player_2_hand)

        i = 0
        while i < len(p1):
            if p1[i] > p2[i]:
                return 'Player 1 wins'
            elif p1[i] < p2[i]:
                return 'Player 2 wins'
            elif i == len(p1) - 1:
                return 'Draw'
            i += 1

    elif hand_rank == 'Flush':
        # SAME AS HIGH CARD
        # sort hands in list and compare last list items
        # if they are the same print draw
        # if player 1 > player 2 print player 1 wins else player 2 wins
        p1, p2 = sort_ranks(player_1_hand, player_2_hand)

        i = 0
        while i < len(p1):
            if p1[i] > p2[i]:
                return 'Player 1 wins'
            elif p1[i] < p2[i]:
                return 'Player 2 wins'
            elif i == len(p1) - 1:
                return 'Draw'
            i += 1

    elif hand_rank == 'Full House':
        # SAME AS THREE OF A KIND
        # get keys with value 3
        # if player 1 > player 2 print player 1 wins else player 2 wins
        pair_1 = 0
        pair_2 = 0

        for key, value in player_1_hand.items():
            if value == 3:
                pair_1 = enumerate_ranks[key]

        for key, value in player_2_hand.items():
            if value == 3:
                pair_2 = enumerate_ranks[key]

        if pair_1 > pair_2:
            return 'Player 1 wins'
        else:
            return 'Player 2 wins'

    elif hand_rank == 'Four of a Kind':
        # get keys with value 4
        # if player 1 > player 2 print player 1 wins else player 2 wins
        pair_1 = 0
        pair_2 = 0

        for key, value in player_1_hand.items():
            if value == 4:
                pair_1 = enumerate_ranks[key]

        for key, value in player_2_hand.items():
            if value == 4:
                pair_2 = enumerate_ranks[key]

        if pair_1 > pair_2:
            return 'Player 1 wins'
        else:
            return 'Player 2 wins'

    elif hand_rank == 'Straight Flush':
        # SAME AS HIGH CARD
        # sort hands in list and compare last list items
        # if they are the same print draw
        # if player 1 > player 2 print player 1 wins else player 2 wins
        p1, p2 = sort_ranks(player_1_hand, player_2_hand)

        i = 0
        while i < len(p1):
            if p1[i] > p2[i]:
                return 'Player 1 wins'
            elif p1[i] < p2[i]:
                return 'Player 2 wins'
            elif i == len(p1) - 1:
                return 'Draw'
            i += 1


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

    return 'Something went wrong, evaluation is not correct'


player_1, player_2 = deal_cards(initialize_deck())

print(f'Player 1 cards: {player_1}')
print(f'Player 2 cards: {player_2}')
print('\n')
print(f'Player 1 hand ranking: {hand_category(player_1)}')
print(f'Player 2 hand ranking: {hand_category(player_2)}')
print('\n')

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

