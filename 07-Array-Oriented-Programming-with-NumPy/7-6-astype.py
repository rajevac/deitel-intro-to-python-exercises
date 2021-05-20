import numpy as np

# 2 x 3

arr = np.linspace(1.1, 6.6, 6).reshape(2, 3)
print(arr)

arr = arr.astype('int')
print(arr)