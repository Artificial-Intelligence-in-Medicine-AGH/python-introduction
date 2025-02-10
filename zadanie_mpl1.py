import matplotlib.pyplot as plt
import numpy as np


a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))

f = lambda x: a * x**2 + b * x + c

tabx = np.linspace(-10,10.1,201, retstep=False, endpoint=False)
taby = f(tabx)

plt.plot(tabx,taby)
plt.plot()

plt.axvline(x=0, color = 'k')
plt.axhline(y=0, color = 'k')
plt.grid(True)


plt.show()

