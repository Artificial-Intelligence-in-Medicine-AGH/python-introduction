import numpy as np

arr = np.random.randint(1, 101, 20)
avg = np.average(arr)

print(arr)
print(f"{avg=}")

print("")

arr = np.zeros((4, 5), dtype=int)

for i in range(4):
    for j in range(5):
        arr[i, j] = i * 5 + j

arr *= 2

arr = arr.reshape((2, 10))

print(arr)
