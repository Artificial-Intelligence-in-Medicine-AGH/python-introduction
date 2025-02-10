import matplotlib.pyplot as plt
import numpy as np

#zadanie 2
tab = np.random.randint(0, 20, 100)

x, y = np.unique(tab, return_counts=True)
plt.bar(x, y, color="hotpink")

font1 = {'family':'serif','color':'purple','size':12}
plt.title("Wykres słupkowy ilości poszczególnych liczb", fontdict= font1)
plt.xlabel("liczby", fontdict= font1, loc = 'right')
plt.ylabel("ilość", fontdict= font1, loc = 'top')
plt.xticks(x)

plt.show()