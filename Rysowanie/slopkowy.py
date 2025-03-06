import matplotlib.pyplot as plt
import numpy as np

tab = np.random.randint(1,10,size=100)

wartosci, wystapienia = np.unique(tab,return_counts=True)

plt.bar(wartosci,wystapienia)

plt.xticks(wartosci)


plt.title("Wystąpienia liczb losowych")
plt.xlabel("Wartości")
plt.ylabel("Wystąpienia")

plt.show()