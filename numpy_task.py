import numpy as np
import matplotlib.pyplot as plt
print(numpy.__version__)
print(matplotlib.__version__)


# zad 1 python
def sortuj(tab):
    for i in range(len(tab)):
        for j in range(1, len(tab) - i):
            if tab[j-1] > tab[j]:
                tab[j-1], tab[j] = tab[j], tab[j-1]
    return tab



def policz(liczba, lista):
    licznik = 0
    for i in lista:
        if i == liczba:
            licznik += 1
    return licznik

import random
randomlist = []

for i in range(20):
    randomlist.append(random.randint(0, 5))

posortowana = sortuj(randomlist)

for i in range(6):  # Liczby od 0 do 5
    print(f'"{i}" - {policz(i, posortowana)}')

# zad 2 numpy

tab = np.random.randint(1, 101, size=20)

srednia = np.mean(tab)

tablicka = np.zeros((4, 5))

wartosc = 0
for i in range(tablicka.shape[0]):  
    for j in range(tablicka.shape[1]): 
        tablicka[i, j] = wartosc
        wartosc += 1


tablicka = tablicka*2
tablicka = tablicka.reshape(2,10)

print(tablicka)

# zad 2 Matplotlib

import matplotlib.pyplot as plt

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

x = np.arange(-10, 10.1, 0.1)  # 10.1 żeby włączyć 10 w siatkę
y = a * x**2 + b * x + c

plt.plot(x, y, label=f"y = {a}x^2 + {b}x + {c}", color="red")

plt.axhline(0, color='black', linewidth=1)

plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.grid(True) #siatka wykresu
plt.show()

# zad 2.2

tab_do_matplot = np.random.randint(1, 101, size=100)

unikatowe, liczby = np.unique(tab_do_matplot, return_counts=True)

plt.bar(unikatowe, liczby, color="white", edgecolor="black")
plt.title("Rozklad losowy")


plt.show()