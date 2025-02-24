import numpy as np
import matplotlib.pyplot as plt

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

x = np.arange(-10, 10, step=0.1)
y = a*(x**2) + b*x + c

plt.plot(x, y)
plt.title("Funkcja kwadratowa (-10, 10)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()