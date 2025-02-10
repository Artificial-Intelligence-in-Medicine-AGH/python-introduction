import matplotlib.pyplot as plt
import numpy as np

#zadanie 1
print("Podaj współczynniki a,b,c funkcji kwadratowej w postaci y = ax^2 + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

xpoints = np.arange(-10, 10.1, 0.1)
ypoints = a * xpoints**2 + b * xpoints + c

font1 = {'family':'serif','color':'blue','size':15}

plt.title("Wykres funkcji kwadratowej", fontdict= font1)
plt.xlabel("x", fontdict= font1, loc = 'right')
plt.ylabel("y", fontdict= font1, loc = 'top')

plt.plot(xpoints, ypoints, label=f"y={round(a,2)}x² + {round(b,2)}x + {round(c,2)}", color="red")

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

plt.grid(True, color="grey", linestyle="--", linewidth=0.5)

plt.legend()
plt.show()
