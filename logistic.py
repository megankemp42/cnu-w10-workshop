import matplotlib.pyplot as plt
import numpy as np

def nextx(a, x):
    return a * x * (1 - x)

def map(a, x0, n, colour):
    xks = [x0]
    for i in range(1, n):
        xks.append(nextx(a, xks[i-1]))
    ax.plot(np.linspace(1, n, n), xks, color=colour, linestyle='-', linewidth=0.8, label=f'a = {a}')

x0 = np.random.rand()

#colours = ['magenta', 'green', 'purple', 'blue']
#avals = [2.7, 3.1, 3.5, 3.7]

#for i in range(0, 4):
#    map(avals[i], x0, 200, colours[i])

fig, ax = plt.subplots(figsize=(16, 8))

a = 2.5
x0 = np.random.rand(1)
xks = [x0]

while a <= 3.8:
    for i in range(1, 101):
        ax.plot(i, xks[-1], color=[0.1]*4, marker='o', markersize=2)
        if i != 100:
            xks.append(nextx(a, xks[i-1]))
        else:
            a += 0.025
            break
    xks = [xks[-1]]

#ax.legend(loc='best')

plt.show()