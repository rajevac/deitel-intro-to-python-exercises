items = []


def enqueue(item):
    items.append(item)


def dequeue():
    if len(items) > 0:
        items.pop(0)


enqueue(5)
enqueue(11)
enqueue('Jones')
enqueue(45)

print(items)

dequeue()
print(items)

dequeue()
print(items)