import numpy as np

lista = np.zeros((4,5),dtype=int)

for i in range(4):
    for j in range(5):
        lista[i][j] = j + i * 5

print(lista)

lista = lista * 2

print(lista)

lista = lista.reshape((2,10))

print(lista)