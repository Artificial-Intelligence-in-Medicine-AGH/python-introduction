import numpy as np

arr = np.array([0]*20)
avg = 0
for indx in range(0,len(arr)):
    arr[indx] = np.random.randint(1,101)
    avg += arr[indx]
avg /= len(arr)
print("array: ")
print(arr)
print("\navarage value: ", avg)