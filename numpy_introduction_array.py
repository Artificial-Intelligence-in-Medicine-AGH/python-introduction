import numpy as np

def main():
    list = [[0]*5 for row in range(4)]
    arr = np.array(list)
    for i in range(4):
        for j in range(5):
            arr[i,j]=(i*5)+j
    arr*=2
    arr = arr.reshape((2,10))
    print(arr)

if __name__ == '__main__':
    main()