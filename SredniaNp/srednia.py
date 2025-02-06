import numpy as np

lista = []

for i in range(20):
    liczba = np.random.randint(1,101)
    lista.append(liczba)

srednia = np.mean(lista)

print(lista,srednia)

