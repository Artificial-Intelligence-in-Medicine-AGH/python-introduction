import random as r

def podziel(lista,start,end):
    pivot = lista[end]
    j = start - 1
    for i in range(start,end):
        if lista[i] < pivot:
            j+=1
            lista[i],lista[j] = lista[j],lista[i]
    
    lista[j+1],lista[end] = lista[end],lista[j+1]

    return j + 1

def sortuj(lista,start,end):
    if end <= start: return

    pivot = podziel(lista,start,end)

    sortuj(lista,start,pivot-1)
    sortuj(lista,pivot+1,end)

def policz(liczba,lista):
    counter = 0
    for num in lista:
        if num == liczba:
            counter+=1 
    return counter

lista = []

for i in range(20):
    liczba = r.randint(0,5)
    lista.append(liczba)

sortuj(lista,0,len(lista) - 1)

i = 0
while i <= 5:
    print(f'"{i}" - {policz(i,lista)}')
    i+=1