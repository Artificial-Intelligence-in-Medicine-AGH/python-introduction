import matplotlib.pyplot as plt
import numpy as np

def quadric(a,b,c,x):
    return a*pow(x, 2)+b*x+c

def main():
    a = float(input("Insert a: "))
    b = float(input("Insert b: "))
    c = float(input("Insert c: "))
    xpoints = np.linspace(-10,10,num=201)
    ypoints = quadric(a,b,c, xpoints)
    plt.plot(xpoints, ypoints)

    plt.axhline(0, color='black', linewidth=.5)
    plt.axvline(0, color='black', linewidth=.5)

    plt.xticks(np.arange(-10, 11))

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Quadric function graph')

    plt.show()

if __name__ == '__main__':
    main()