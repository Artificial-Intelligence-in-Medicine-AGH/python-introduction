import random

def sortuj(lista):
    n = len(lista)
    for i in range(n):
        for j in range(1, n-i):
            if lista[j-1]>lista[j]:
                lista[j-1],lista[j] = lista[j], lista[j-1]

def policz(liczba, lista):
    counter = 0
    for item in lista:
        if item == liczba:
            counter += 1
    return counter

def main():
    list = []
    for _ in range(20):
        list.append(random.randint(0,5))

    sortuj(list)
    print(list)

    for i in range(6):
        print(f"\"{i}\"-{policz(i, list)}")

if __name__ == '__main__':
    main()