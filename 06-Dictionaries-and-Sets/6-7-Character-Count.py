import string

sentence = input()

sentence = sentence.lower()
sentence = sentence.replace(' ', '')
char_count = {}
alphabet = set(string.ascii_lowercase)

for i in range(len(sentence)):
    if sentence[i] in char_count:
        char_count[sentence[i]] += 1
    else:
        char_count[sentence[i]] = 1

char_in_sentence = []
print(f'{"character":<12}count')
for key, value in sorted(char_count.items()):
    char_in_sentence.append(key)
    print(f'{key:<12}{value}')

char_in_sentence = set(char_in_sentence)
print(f'Alphabet characters not in the sentence: {alphabet.difference(char_in_sentence)}')

