import numpy as np

def main():
    arr = np.random.randint(1, high=101, size=20)
    print(arr)
    sum_of_arr = sum(arr)
    print(sum_of_arr / 20)

if __name__ == '__main__':
    main()