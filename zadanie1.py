import random

def policz(liczba: int, lista):
    rtr = 0
    for l in lista:
        if l == liczba:
            rtr += 1
    
    return rtr


def sortuj(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    

    return lista



lista = []
for i in range(20):
    lista.append(random.randint(0,5))


sortuj(lista)

i = 0
while i<=5:
    print(f'"{i}" - {policz(i,lista)}')
    i += 1

