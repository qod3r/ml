import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from math import cos, sin
import numpy as np


f1 = lambda x: cos(x) + 2.9
f2 = lambda x: -sin(x) + 1.2

dotx, doty = [], []
for i in range(100):
    x = np.random.rand() * 3.25 + 0.5
    ymax = f1(x)
    ymin = f2(x)
    y = np.random.uniform(ymin + 0.1, ymax - 0.1)
    dotx.append(x)
    doty.append(y)
    

fig = plt.figure()
ax = fig.add_subplot()

plt.xlabel("Подпись оси OX")
plt.ylabel("Подпись оси ОY")
plt.title("Элементы изображения")

ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.xaxis.set_minor_formatter('{x:.2f}')

ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))

ax.plot(np.arange(0.5, 4, 0.25), [f1(x) for x in np.arange(0.5, 4, 0.25)], label="Синяя линия")
ax.plot(np.arange(0.5, 4, 0.25), [f2(x) for x in np.arange(0.5, 4, 0.25)], label="Красная линия", c='r')
ax.scatter(dotx, doty, edgecolors='black', marker='o', facecolors='none', s=30)

ax.tick_params(axis='x', which='minor', labelsize=7)
ax.set_xlim(xmin=0)
ax.set_aspect('equal')
ax.grid(c='black', linestyle='--', which='major')
ax.legend()

plt.savefig("fig2.png")