import numpy as np

tab = np.array([0]*20)
for i in range(20):
    tab[i] = np.random.randint(0,101)

srednia = np.average(tab)
print(f'Tablica: {tab}| Średnia: {srednia}')


