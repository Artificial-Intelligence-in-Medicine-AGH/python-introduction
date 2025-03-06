import numpy as np

r, k = 4, 5
tab = np.zeros((r, k), dtype=int)
licznik = 0
for i in range(r):
    for j in range(k):
        tab[i, j] = licznik
        licznik += 1

tab *= 2

tablica = tab.reshape(2, 10)

print("Nowa tablica:")
print(tab)