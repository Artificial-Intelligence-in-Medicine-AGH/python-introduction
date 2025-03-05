import numpy as np
arr = np.zeros((4,5))
number = 1
for i, x in np.ndenumerate(arr):
    if number % 2 == 0:
        arr[i] = 1
    else:
        arr[i] = 0
    number += 1
arr *= 2
arr.reshape(2,10)

print(arr)