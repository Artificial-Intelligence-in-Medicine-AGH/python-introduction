import numpy as np
import matplotlib.pyplot as plt


losowe_liczby = np.random.randint(0, 10, 100)


unikalne, liczby_wystapien = np.unique(losowe_liczby, return_counts=True)


plt.bar(unikalne, liczby_wystapien, color='skyblue', edgecolor='black')


plt.xlabel('liczby')
plt.ylabel('wystąpienia')
plt.title('liczby z numpy')



plt.show()