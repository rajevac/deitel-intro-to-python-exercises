two_d_list = [[11, 21], [12, 22], [13, 23], [14, 24], [15, 25], [16, 26], [17, 27]]


def print_2d_list(list_2d):
    print(f'{0:>3} {1:>2}')
    for idx in range(len(list_2d)):
        print(f'{ idx } { list_2d[idx][0] } { list_2d[idx][1] }')


print_2d_list(two_d_list)

