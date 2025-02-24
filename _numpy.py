import numpy as np

print("ZADANIE 1")

arr = np.random.randint(101, size=20)
print(f"Lista: {arr}")
print(f"Średnia: {arr.mean()}")


print("\nZADANIE 2")

arr1 = np.zeros((4, 5), dtype=int)
counter = 0
for i in range(4):
    for j in range(5):
        arr1[i, j] = counter
        counter += 1

arr1 *= 2

arr1 = arr1.reshape((2, 10))
print(f"Lista: {arr1}")
