import numpy as np
from numpy import random

def wypisz_tablice(lista, zakres):
    print("Tablica liczb : ", end="")
    for i in range(zakres):
        print( lista[i] , " ",  end="")

def srednia_liczb(lista, zakres):
    wypisz_tablice(lista, zakres)
    print("\nSrednia liczb wynosi: ", np.mean(lista))

lista = []
zakres = 20

for i in range(zakres):
    number = random.randint(100) + 1
    lista.append(number)
    
srednia_liczb(lista, zakres)






# import random

# def sortuj(lista, zakres):
#     for i in range(zakres-1):
#         for j in range(zakres-1):
#             if lista[j] > lista[j+1]:
#                 temp = lista[j]
#                 lista[j] = lista[j+1]
#                 lista[j+1] = temp
                
# def policz(lista, zakres):
#     i = 0
#     while i <= 5:
#         print(f"\"{i}\" - " ,  lista.count(i))
#         i+=1

# lists = []
# zakres = 20

# for number in range(zakres):
#     number = random.randrange(6)
#     lists.append(number)

# sortuj(lists, zakres)
# policz(lists, zakres)

# for n in range(zakres):
#     print(lists[n])
    