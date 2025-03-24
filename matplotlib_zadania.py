import numpy as np
import matplotlib.pyplot as plt

#zadanie 1

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

x = np.linspace(-10, 10, 200)
y = a * x**2 + b * x + c
plt.plot(x, y, label="y = ax^2 + bx + c")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres funkcji kwadratowej")


#plt.axhline(0, color='black',linewidth=1)
#plt.axvline(0, color='black',linewidth=1)


plt.grid(True)
plt.legend()
plt.show()



#zadanie 2
random_numbers = np.random.randint(0, 6, 100)
values, counts = np.unique(random_numbers, return_counts=True)

plt.bar(values, counts)

plt.xlabel("Liczby")
plt.ylabel("Ilość wystąpień")
plt.title("Wykres słupkowy liczb losowych")

plt.show()