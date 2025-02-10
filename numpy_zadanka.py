import numpy as np

#zadanie 1
tab = np.random.randint(1, 101, 20)
avg = np.average(tab)
print("[", ", ".join(map(str, tab)), "]" )
print(f"Średnia = {avg}")

print("")

#zadanie 2
tab2 = np.zeros((4,5), dtype=int)

liczba = 0
for i in range(4):
    for j in range(5):
        tab2[i,j] = liczba
        liczba+=1

tab2 *=2
tab2_reshaped = tab2.reshape((2,10))

print(f"Końcowa tablica:\n {tab2_reshaped}")