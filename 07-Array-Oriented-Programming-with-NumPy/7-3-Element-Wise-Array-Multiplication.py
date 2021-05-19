import numpy as np

arr_1 = np.arange(2, 19, 2).reshape(3, 3)
print(arr_1)

arr_2 = np.arange(9, 0, -1).reshape(3, 3)
print(arr_2)

print(arr_1 * arr_2)