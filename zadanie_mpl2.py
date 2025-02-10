import matplotlib.pyplot as plt
import numpy as np


tab = np.array([0]*100)

for i in range(len(tab)):
    tab[i] = np.random.randint(0,10)

histogram = np.array([0]*10)
for t in tab:
    histogram[t] += 1

plt.bar(np.linspace(0,9,10), histogram)
plt.xticks(np.linspace(0,9,10))
plt.show()
