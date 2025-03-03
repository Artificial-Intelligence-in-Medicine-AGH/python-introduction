import numpy as np
tab = np.zeros((4, 5))

temp = 0
for i in range(4):
    for j in range(5):
       tab[i][j] = temp
       temp += 1 
       
tab*=2
tab = tab.reshape((2, 10))

print(tab)