import random
import numpy as np

nums = [random.randint(1, 10) for x in range(50)]

# print(nums)
# print(np.unique(nums, return_counts=True))

values, frequencies = np.unique(nums, return_counts=True)

for index, value in enumerate(values):
    print(f'value: {value} -> frequency: {frequencies[index]}')

