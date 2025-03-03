import random

def sortuj(lista):
    return sorted(lista)

def policz(liczba, lista):
    
    return lista.count(liczba)


lista_liczb = [random.randint(0, 5) for _ in range(20)]

lista_liczb = sortuj(lista_liczb)

i = 0
while i <= 5:
    print(f'"{i}" - {policz(i, lista_liczb)}')
    i += 1

