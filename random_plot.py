import numpy as np
import matplotlib.pyplot as plt
# range of random numbers - [1,10]
array = np.array( [np.random.randint(1,11) for x in range(100)])
#print(array)

counting_array = np.array([0]*10)
for x in array:
    counting_array[x-1] += 1
print(counting_array)

plt.bar(np.arange(1,11), counting_array)
plt.xlabel("drawn integer")
plt.ylabel("number of occurences")
plt.title("amount of each [1,10] number within 100 randomly drawn")
plt.xticks(np.arange(1,11))
plt.show()