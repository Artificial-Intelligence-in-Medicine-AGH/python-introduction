import matplotlib.pyplot as plt
import math
import numpy as np
def funkcja(a, b, c, x):
    return a*(x*x)+(b*x)+c
print("Witaj! Czas narysować Twoją funkcję w postaci ax^2+bx+c=0. Zaczynamy!")
a= int(input("Podaj współczynnik a: "))
b= int(input("Podaj współczynnik b: "))
c= int(input("Podaj współczynnik c: "))


plt.figure(figsize=(10,8), dpi=100)
x=np.linspace(-10, 10, num=201)
y=funkcja(a, b, c, x)

plt.xlabel('oś x')
plt.ylabel('oś y')
plt.axhline(y=0, color="#cccccc")
plt.axvline(x=0, color="#cccccc")
plt.title(f"Wykres funkcji {a}x^2+{b}x+{c}")

plt.plot(x,y)
plt.show()

