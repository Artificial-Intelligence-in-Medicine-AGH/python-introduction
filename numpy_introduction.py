import numpy as np

# Zadanie 1
random_numbers = np.random.randint(1, 101, size=20)

average = np.mean(random_numbers)

print("Wygenerowana tablica liczb:", random_numbers)
print("Średnia arytmetyczna:", average)


# Zadanie 2
array_to_reshape = np.zeros((4, 5), dtype=int)
for i in range(4):
    for j in range(5):
        array_to_reshape[i, j] = i * 5 + j

array_to_reshape *= 2

array_reshaped = array_to_reshape.reshape((2, 10))

print(array_reshaped)