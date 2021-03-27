numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(result)

# a) 10 times
# b) 5 times

result = list(map(lambda x: x % 2 != 0, filter(lambda x: x ** 2, numbers)))
print(result)
# c) 10 times

result = []
count = 1
for num in numbers:
    if num % 2 != 0:
        print(count)
        count += 1
        result.append(num ** 2)

print(result)

result = []
count = 1
for num in numbers:
    num = num ** 2
    result.append(num % 2 != 0)
    print(count)
    count += 1

print(result)

