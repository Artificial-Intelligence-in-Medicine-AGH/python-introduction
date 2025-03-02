import numpy as np
import matplotlib.pyplot as plt
data = np.random.randint(1, 11, size=100)
unique, counts = np.unique(data, return_counts=True)
plt.bar(unique, counts)
plt.title("Rozkład wystąpień liczb losowych")
plt.xlabel("Liczba")
plt.ylabel("Ilość wystąpień")
plt.show()