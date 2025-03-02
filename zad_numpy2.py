import numpy as np

tablica=np.zeros((4,5), dtype=int)
n=0
for i in range (0,4):
    for j in range (0,5):
        tablica[i][j]=n
        n+=1
np.multiply(tablica, 2, out=tablica)
tablica=tablica.reshape(2,10)
print(tablica)

     
