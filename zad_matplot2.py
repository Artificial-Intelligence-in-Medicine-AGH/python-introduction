import matplotlib.pyplot as plt
import numpy as np
random_numbers = np.random.randint(1, 7, size=100)
liczby, ilosc = np.unique(random_numbers, return_counts=True)

plt.bar(liczby, ilosc, color='darkblue', edgecolor='pink', alpha=0.5)
plt.title("Wykres słupkowy liczb losowych")
plt.xlabel("Liczba")
plt.ylabel("Ilość wystąpień")
plt.show()