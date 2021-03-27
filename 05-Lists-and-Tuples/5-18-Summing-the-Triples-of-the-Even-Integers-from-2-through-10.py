nums = []

for num in range(2, 11):
    nums.append(num)

# using sum, map and filter
result = sum(list(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, nums))))
print(result)

# list comprehensions
result = sum([num * 3 for num in range(2, 11) if num % 2 == 0])
print(result)

