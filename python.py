import random

def sortuj(lista):
    n = len(lista)
    for i in range(n):
        for j in range(1, n - i):
            if lista[j - 1] > lista[j]: 
                lista[j - 1], lista[j] = lista[j], lista[j - 1]
    
def policz(lista, liczba):
    x=0 
    for i in range(len(lista)):
        if lista[i]==liczba:
            x=x+1
    return x

lista1=[]
for i in range(20):
    lista1.append(random.randint(0,5))
print(lista1)
for i in range(6):
    print(str(i)+" - "+ str(policz(lista1, i)))