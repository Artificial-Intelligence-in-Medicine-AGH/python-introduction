import numpy as np
import matplotlib.pyplot as plt
tablica=np.random.randint(0,5,100)
unikalne, unikalne_liczba = np.unique(tablica, return_counts=True)  
supek=plt.bar(unikalne, unikalne_liczba)
plt.xlabel('pracownicy')
plt.xticks(unikalne,["Asia", "Kasia", "Basia", "Stasia", "Jasia"])
plt.ylabel('wynagrodzenie')
plt.title('------SŁUPKI-----')
plt.bar_label(supek)
plt.show()