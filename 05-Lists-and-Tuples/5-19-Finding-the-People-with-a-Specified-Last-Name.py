names = [('Bradford', 'Jones'),
         ('Cyprian', 'Azure'),
         ('Eustace', 'Archer'),
         ('Edythe', 'Harrison'),
         ('Philander', 'Jones'),
         ('Eveleen', 'Jones'),
         ('Nikola', 'Ethelred'),
         ('Stewart', 'Jones'),
         ('Martin', 'Irvine'),
         ('Colleen', 'Andrina')]

result = list(filter(lambda x: x[1] == 'Jones', names))
print(result)

