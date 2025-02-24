import numpy as np
import matplotlib.pyplot as plt

rand_numbers = np.random.randint(0, 44, 100)
val, counts = np.unique(rand_numbers, return_counts=True)

plt.bar(val, counts)
plt.title("Histogram wystąpień")
plt.xlabel("liczba")
plt.ylabel("wystąpienia")
plt.show()
