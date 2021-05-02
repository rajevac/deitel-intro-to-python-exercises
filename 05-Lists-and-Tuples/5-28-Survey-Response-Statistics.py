import numpy as np
from scipy import stats

ratings = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

print(f'maximum: {np.max(ratings)}')
print(f'minimum: {np.min(ratings)}')
print(f'range: {np.max(ratings) - np.min(ratings)}')
print(f'mean: {np.mean(ratings)}')
print(f'median: {np.median(ratings)}')
print(f'mode: {stats.mode(ratings)[0]}')
print(f'standard deviation: {np.std(ratings)}')
print(f'variance: {np.var(ratings)}')