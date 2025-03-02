import numpy as np
import matplotlib.pyplot as plt
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

x = np.arange(-10, 10, 0.1)
y = a * x**2 + b * x + c
plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')

plt.title("Wykres funkcji kwadratowej")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.show()