set_1 = {'red', 'green', 'blue'}
set_2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

# a
print(set_1 == set_2)
print(set_1 != set_2)
print(set_1 > set_2)
print(set_1 < set_2)
print(set_1 <= set_2)
print(set_1.issubset(set_2))
print(set_1 >= set_2)
print(set_1.issuperset(set_2))

# b
print(set_1 | set_2)
print(set_1 & set_2)
print(set_1 - set_2)
print(set_1 ^ set_2)
print(set_1.isdisjoint(set_2))