# let's begin spaghetti code by Dżejkob Taranek
# The comments in the code are in English specifically for Dominik :P
from numpy import random
import numpy as np

def compute_mean(narr):
    mean = 0
    for num in narr:
        mean += num
    mean /= narr.size
    return mean

ARR_SIZE = 20
arr = random.randint(1,101, size = ARR_SIZE)

print("Array: ", arr)
print("Mean:  " , compute_mean(arr))
print("Np Mean: ", np.mean(arr))