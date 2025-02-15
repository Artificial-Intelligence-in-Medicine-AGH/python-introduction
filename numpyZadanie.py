import numpy as np

arr = np.random.randint(1,101, size=10)

x = np.average(arr)

print(arr)
print(f"srednia z liczb w wylosowanej liscie: {x}")