import numpy as np

tab = np.zeros((4, 5))

wartosc = 0
for i in range(tab.shape[0]):  # Pętla po wierszach
    for j in range(tab.shape[1]):  # Pętla po kolumnach
        tab[i, j] = wartosc
        wartosc += 1


tab = tab*2
tab = tab.reshape(2,10)
print(tab)