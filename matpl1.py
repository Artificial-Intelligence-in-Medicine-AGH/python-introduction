import numpy as np
import matplotlib.pyplot as plt


a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))


x = np.linspace(-10, 10, 200)  
y = a * x**2 + b * x + c

plt.plot(x, y, label=f'${a}x^2 + {b}x + {c}$', color='blue')

plt.axhline(0, color='black', linewidth=0.8)  
plt.axvline(0, color='black', linewidth=0.8)  


plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres funkcji kwadratowej")
plt.legend()
plt.grid()


plt.show()
