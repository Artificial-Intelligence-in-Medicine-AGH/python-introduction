
try:
    import numpy as np
except ImportError:
    print("Numpy is not installed. Please install it using 'pip install numpy'.")

# zadanie 1
random_numbers = np.random.randint(1, 101, 20)
mean = np.mean(random_numbers)
print("Tablica liczb:", random_numbers)
print("Średnia:", mean)

# zadanie 2
zeros_array = np.zeros((4, 5), dtype=int)

count = 0
for i in range(4):
    for j in range(5):
        zeros_array[i, j] = count
        count += 1

zeros_array *= 2
reshaped_array = zeros_array.reshape(2, 10)
print("Nowa tablica 2x10:")
print(reshaped_array)