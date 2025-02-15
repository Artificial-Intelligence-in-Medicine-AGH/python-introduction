import random

def sortuj(lista):
    lista.sort() 
    return lista

def policz(liczba, lista):
    return lista.count(liczba)

lista = [5,6,1,4,2,2,9,0]

print(lista)
sortuj(lista)
print(lista)

x = 2
print(f"ilosc wystapienia {x} w liscie = {policz(x, lista)}")


#------------------------
lista = [random.randint(0, 5) for _ in range(20)]
print(lista)

posortowana_lista = sortuj(lista.copy()) 

i = 0
while i <= 5:
    liczba_wystapien = policz(i, posortowana_lista)
    print(f"Liczba {i} występuje {liczba_wystapien} razy.")
    i += 1
