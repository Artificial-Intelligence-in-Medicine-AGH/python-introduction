import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.axisartist.axislines import AxesZero

print("Enter coefficients for quadratic formula: ax^2 + bx + c:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

minX = -10
maxX = 10
step = 0.1
XsCount = int((maxX - minX) / step) + 1

Xs = np.array(np.linspace(minX, maxX, XsCount))
Ys = np.array([a*(x**2) + b*x + c for x in Xs])

fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)

plt.gcf().canvas.manager.set_window_title("Quadratic formula chart")
ax.plot(Xs, Ys)

# adds arrows at the ends of each axis
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

# hides borders
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

ax.legend([f"f(x) = {a}^x + {b}x + {c}"])

plt.show()
