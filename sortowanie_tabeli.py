import random

def sortuj(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def policz(liczba, lista):
    return lista.count(liczba)


losowa_lista = [random.randint(0, 5) for _ in range(20)]
sortuj(losowa_lista)
print("Posortowana lista:", losowa_lista)

i = 0
while i <= 5:
    # Wywołanie funkcji policz dla liczby i
    liczba_wystapien = policz(i, losowa_lista)
    print(f'"{i}" - {liczba_wystapien}')
    i += 1