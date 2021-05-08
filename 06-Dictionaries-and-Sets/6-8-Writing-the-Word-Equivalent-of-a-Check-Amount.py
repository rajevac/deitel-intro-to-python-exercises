num_word = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE',
            6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', 10: 'TEN',
            11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN', 15: 'FIFTEEN',
            16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY',
            30: 'THIRTY', 40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY',
            80: 'EIGHTY', 90: 'NINETY', 100: 'HUNDRED'}

num_1 = '7.20'
num_2 = '99.45'
num_3 = '321.75'

dollars, cents = num_3.split('.')


def find_number(first_num, second_num):
    first_num = int(first_num)
    second_num = int(second_num)
    if first_num == 0:
        return num_word[second_num]
    elif second_num == 0:
        return num_word[first_num * 10]
    elif first_num == 1:
        return num_word[first_num * 10 + second_num]
    else:
        return f'{num_word[first_num * 10]}{num_word[second_num]}'


def dollars_and_cents(dollars, cents):
    if len(str(dollars)) == 1:
        dollars = int(dollars)
        print(f'{num_word[dollars]} AND {cents}/100')

    if len(str(dollars)) == 2:
        print(f'{find_number(dollars[0], dollars[1])} AND {cents}/100')

    if len(str(dollars)) == 3:
        print(f'{num_word[int(dollars[0])]} HUNDRED {find_number(dollars[1], dollars[2])} AND {cents}/100')


dollars_and_cents(dollars, cents)





