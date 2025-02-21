import numpy as np

# arr = np.array([[0]*5]*4)
# val = 0
# for x in range(0,len(arr)):
#     for y in range(0,len(arr[x])):
#         arr[x][y] = val
#         val += 1

# does the same what lines 3 - 8 do
arr = np.arange(20).reshape(5,4) 

arr = arr * 2 
# alternative -> arr = np.multiply(arr,2)
arr = arr.reshape(2,10)

print(arr)