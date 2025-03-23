import numpy as np


tab = np.random.randint(1, 101, 20, dtype=int)  

srednia = np.mean(tab)

print("Wygenerowana tablica:", tab)
print("srednia:", srednia)

nr=0
array=np.zeros((4,5), dtype=int)
for i in range(4):
 for j in range (5):
     array[i][j]=nr
     nr+=1



array=array*2

newarray=np.reshape(array, (2,10))

print(newarray)



