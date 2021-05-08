text = 'There were doors all round the hall but they were all locked and when Alice had been all the way down one ' \
       'side and up the other trying every doorshe walked sadly down the middle ' \
       'wondering how she was ever to get out again'.lower()

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(f'{key}: {value}')


print(f'Number of words unique in the sentence: {len(word_count)}')