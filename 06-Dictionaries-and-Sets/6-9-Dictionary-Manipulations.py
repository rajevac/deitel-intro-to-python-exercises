tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# a
print('Canada' in tlds)

# b
print('France' in tlds)

# c
for key, value in tlds.items():
    print(f'{key}: {value}')

# d
tlds['Sweden'] = 'sw'

# e
tlds['Sweden'] = 'se'
print(tlds)

# f
tlds2 = {value: key for key, value in tlds.items()}
print(tlds2)

# g
tlds2 = {key: value.upper() for key, value in tlds2.items()}
print(tlds2)