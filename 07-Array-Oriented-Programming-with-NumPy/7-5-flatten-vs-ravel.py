import numpy as np

arr = np.array([2 ** x for x in range(0, 6)]).reshape(2, 3)
print(arr)

flat = arr.flatten()
print(flat)
flat[1] = 555

rav = arr.ravel()
print(rav)
rav[1] = 33

print(arr)
print(rav)
print(flat)