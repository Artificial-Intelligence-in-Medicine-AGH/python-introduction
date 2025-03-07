import matplotlib.pyplot as plt
import numpy as np

arr = np.random.randint(1, 11, 100)
print("liczby: ", arr)

unique, counts = np.unique(arr, return_counts=True)


plt.bar(unique, counts, color='red', edgecolor='black')

plt.xlabel("Liczby")
plt.ylabel("Liczba wystąpień")
plt.title("Ilość wystąpień poszczególnych liczb")

plt.show()