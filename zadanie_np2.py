import numpy as np

tab = np.array([[0]*5]*4)

licznik = 0
for i in range(len(tab)):
    for j in range(len(tab[i])):
        tab[i][j] = licznik
        licznik += 1

tab2 = tab.reshape(2,10)
print(tab2)