import numpy as np

test = np.linspace(0.2, 2.2, 8).reshape(2, 4) * 10
test = test.astype('int')
print(test)


def reimplement_numpy(arr):
    max_num = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (j + 1) == len(arr[i]):
                break
            if arr[i][j] > arr[i][j+1]:
                max_num = arr[i][j]
            else:
                max_num = arr[i][j+1]

    ln = len(str(max_num))
    print('[', end='')
    for i in range(len(arr)):
        if i == 0:
            print('[', end='')
        else:
            print(' [', end='')
        for j in range(len(arr[i])):
            if (j+1) == len(arr[i]):
                if i == (len(arr) - 1):
                    print(f'{arr[i][j]}]]', end='\n')
                else:
                    print(f'{arr[i][j]}]', end='\n')
            else:
                print(f'{arr[i][j]:>{ln}}', end=' ')


reimplement_numpy(test)

