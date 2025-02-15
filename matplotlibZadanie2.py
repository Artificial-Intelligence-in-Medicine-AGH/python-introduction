import matplotlib.pyplot as plt
import numpy as np

arr = np.random.randint(0,10, size=100)

plt.title("Wykres ilości poszczególnych liczb")

labels = np.arange(0,10,1)
values = np.array([np.count_nonzero(arr == val) for val in labels])

plt.bar(labels, values, color='lightblue', edgecolor='black')
plt.xlabel("Liczba")
plt.ylabel("Ilość liczb")

plt.xticks(labels)

plt.show()