import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)

plt.title("Wykres funkcji kwadratowej z podanymi współczynnikami")

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

plt.plot(x, a*x**2 + b*x + c, label=f"{a}x^2+{b}x+{c}")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()