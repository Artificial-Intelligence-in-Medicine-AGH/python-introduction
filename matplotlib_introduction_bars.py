import matplotlib.pyplot as plt
import numpy as np

def main():
    arr = np.random.randint(0, 6, 100)
    unique, unique_counts = np.unique(arr, return_counts=True)

    bar_container = plt.bar(unique, unique_counts)

    plt.bar_label(bar_container)

    plt.xticks(unique)

    plt.xlabel('x')
    plt.ylabel('x counts')

    plt.title('Bars')

    plt.show()

if __name__ == '__main__':
    main()