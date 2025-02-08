import random


def sortuj(lista: list[int]) -> None:
    '''Merge sort'''
    if len(lista) > 1:
        mid = len(lista) // 2
        lewy = lista[:mid]
        prawy = lista[mid:]

        sortuj(lewy)
        sortuj(prawy)

        i = j = k = 0

        while i < len(lewy) and j < len(prawy):
            if lewy[i] < prawy[j]:
                lista[k] = lewy[i]
                i += 1
            else:
                lista[k] = prawy[j]
                j += 1
            k += 1

        while i < len(lewy):
            lista[k] = lewy[i]
            i += 1
            k += 1

        while j < len(prawy):
            lista[k] = prawy[j]
            j += 1
            k += 1



def policz(liczba: int, lista: list[int]) -> int:
    '''Policz returns the count of a specific number in the list'''
    return lista.count(liczba)


lista: list[int] = []
for _ in range(20):
    lista.append(random.randint(0,5))

sortuj(lista)

for i in range(6):
    print(f'"{i}" - {policz(i, lista)}')