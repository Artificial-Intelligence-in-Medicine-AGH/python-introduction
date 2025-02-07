import numpy as np
import matplotlib.pyplot as plt

minNum = 1
maxNum = 15
arr = np.random.randint(minNum, maxNum + 1, 100)
counts = np.zeros(maxNum - minNum + 1, dtype=int)

for num in arr:
    counts[num - minNum] += 1

fig, ax = plt.subplots()

plt.gcf().canvas.manager.set_window_title("Counts of each number")

Xs = np.linspace(minNum, maxNum, maxNum - minNum + 1, dtype=int)
strXs = [str(x) for x in Xs]
ax.bar(strXs, counts)

ax.set_title("Count of each number in the randomly generated array")
ax.set_xlabel("Numbers")
ax.set_ylabel("Counts")

plt.show()
