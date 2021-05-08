sentence = 'There were doors all round the hall but they were all locked and when Alice had been all the way down one ' \
       'side and up the other trying every doorshe walked sadly down the middle ' \
       'wondering how she was ever to get out again'.lower()


def unique_words(text):
    text = text.lower()
    words = set(text.split())
    for word in sorted(words):
        print(word)


unique_words(sentence)

