import matplotlib.pyplot as plt
import numpy as np

print("Podaj współczynniki a, b, c funkcji kwadratowej postaci y=ax^2 +bx +c: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x=np.arange(-10,10,0.1)
y=a*x**2+b*x+c

plt.plot(x, y)
plt.title(f"Wykres funkcji kwadratowej y={a}x^2+{b}x+{c}")
plt.xlabel("x")
plt.ylabel("y")
#plt.axhline(0, color='black',linewidth=1)  
#plt.axvline(0, color='black',linewidth=1) 
#plt.grid(True)
plt.show()