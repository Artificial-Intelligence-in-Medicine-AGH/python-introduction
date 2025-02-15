import numpy as np

arr = np.zeros((4,5))
print(arr)

liczba = 0
for i in range(4):
    for j in range(5):
        arr[i][j] = liczba
        liczba += 1
print(arr)

arr = arr*2
print(arr)

after = arr.reshape((2,10))
print(after)