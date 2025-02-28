import numpy as np

N = 4
M = 5

arr = np.zeros((N,M))
value = 1

for idx , _ in np.ndenumerate(arr):
    arr[idx] = value
    value += 1

arr *= 2

newarr = arr.reshape(2,10)
print("New array:\n", newarr)