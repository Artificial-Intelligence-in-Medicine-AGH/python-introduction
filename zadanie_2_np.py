import numpy as np

a = np.zeros ((4,5), int)


for i in range (4):
    a[i] = np.arange(5*i, 5*(i+1))


a = a * 2



a = a.reshape(2, 10)

print (a)