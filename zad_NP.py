import numpy as np


losowe_l = np.random.randint(1, 101, 20)

srednia = np.mean(losowe_l)

print("Wygenerowana tablica liczb:", losowe_l)
print("Srednia wartosc:", srednia)