
import random

def sortuj(lista: list):
    n = len(lista)
    for i in range(n - 1):  
        for j in range(n - 1 - i): 
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  
    return lista


def policz(lista:list, numer:int):
    return lista.count(numer)

lista=[]
for i in range (0,20):
    lista.append(random.randint(0,5))
print("lista przed sortowaniem: {}" .format(lista))
print("lista po sortowaniu: {}" .format(sortuj(lista)))
print ("lista po przeliczeniu:")
i=0
while i<=5:
    print(f'"{i}" - {policz(lista,i)}')
    i+=1

    
        
