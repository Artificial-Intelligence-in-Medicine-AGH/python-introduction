import random

lista = []
dlugosc = range (20)

for i in dlugosc:
    lista.append(random.randrange(0, 6))


print(lista)

def sortuj(slista, rozmiar):

    for i in range (rozmiar):
        index_min = i

        for j in range (i + 1, rozmiar):
            if (slista[j] < slista[index_min]):
                index_min = j

        temp = slista[i]
        slista[i] = slista[index_min]
        slista[index_min] = temp



    

def policz(liczba, plista):

    index = 0

    for i in plista:

        if (i == liczba): 
   
            index+=1

    return index


print("ilość 0: ", policz(0, lista))
print("ilość 1: ", policz(1, lista))
print("ilość 2: ", policz(2, lista))
print("ilość 3: ", policz(3, lista))
print("ilość 4: ", policz(4, lista))
print("ilość 5: ", policz(5, lista))

sortuj(lista, 19)
print(lista)
 
        




