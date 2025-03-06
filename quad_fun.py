import numpy as np
import matplotlib.pyplot as plt

def quad_val(a : float, b : float, c : float, x : float):
    return a*x*x + b*x + c

print("enter quadratic formula coefficients (ax^2+bx+c): ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

xs = np.arange(-10,10.1,0.1)
xs = np.round(xs,2)
#print(xs)

ys = np.array([0.]*len(xs))
for indx in range(len(ys)):
    ys[indx] = float(quad_val(a,b,c,xs[indx]))
ys = np.round(ys,2) # ??
#print(ys)
y_axis = np.arange(np.minimum(-5,np.min(ys)) - 5, np.max(ys) + 5)

plt.plot(xs,ys, color='r', label = (str(a) + "x^2 + " + str(b) + "x + " + str(c)))
plt.plot(xs, np.array([0]*len(xs)), color = 'b')
plt.plot(np.array([0]*len(y_axis)), y_axis , color = 'b')
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.title("quadratic function")
plt.show()