import matplotlib.pyplot as plt
import numpy as np


print("Podaj współczynniki a, b, c funkcji kwadratowej")
print("a: ")
a = float(input())

print("b: ")
b = float(input())

print("c: ")
c = float(input())

x = np.arange(-10, 10, 0.1)
y = a * x**2+ b * x + c

plt.axhline(0, color = "grey")
plt.axvline(0, color = "grey")

plt.title("Funkcja kwadratowa")

plt.xlabel("Oś x")
plt.ylabel("Oś Y")

plt.plot(x, y)
plt.show()