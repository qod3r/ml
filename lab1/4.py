from math import exp, log, sin, tan
import matplotlib.pyplot as plt
import numpy as np


f = lambda x: log((x*x + 1) * exp(-abs(x)/10), 1 + tan(1 / (1 + sin(x) ** 2)))
x = np.arange(-10, 10, 0.25)
y = [f(a) for a in x]

plt.plot(x, y)
plt.savefig("fig4.png")