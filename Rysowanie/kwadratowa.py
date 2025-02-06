import matplotlib.pyplot as plt
import numpy as np

a,b,c = map(float,input("Podaj a, b ,c: ").split())

xTab = np.arange(-10,10,step=0.1)

yTab = np.array([a * x**2 + b * x + c for x in xTab],dtype=float)

plt.plot(xTab,yTab,label=f"{a}x^2 + {b}x + {c}")

plt.axhline(0, color='red', linewidth=1 , label="x")
plt.axvline(0, color='blue', linewidth=1, label="y")

plt.grid()
plt.legend()
plt.show()
