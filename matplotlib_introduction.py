import numpy as np

import matplotlib.pyplot as plt


a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))


def funkcja_kwadratowa(x):
    return a * x**2 + b * x + c


x = np.arange(-10, 10.1, 0.1)
y = funkcja_kwadratowa(x)


plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres funkcji kwadratowej')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()