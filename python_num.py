import numpy as np
lista= []
for i in range(4):
    lista.append([])
    for j in range(5):
        lista[i].append(0)

tablica= np.array(lista)

for i in range(4):
    for j in range(5):
       tablica[i,j]=(i*5)+j

tablica=tablica*2
tablica=tablica.reshape((2,10))
print(tablica)