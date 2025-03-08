import numpy as np

array = np.zeros((4, 5))
for i in range(4):
    for j in range(5):
        array[i][j] = i + j
        
array = np.reshape(array, (2, 10))
print(array)