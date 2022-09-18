import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot()

f = lambda x: x*x - x - 6
x = np.arange(-5, 5, 0.5)
y = f(x)
Oy = np.zeros(x.shape)

# print("x:\n", x, "\ny:\n", y, "\nOy:\n", Oy)

ax.plot(x, y)
ax.plot(x, Oy)
ax.grid()
ax.set_xticks(np.arange(-5, 5, 1))

# idx = np.argwhere(np.diff(np.sign(Oy - f(x)))).flatten()
# print(x[idx], y[idx])
# ax.plot(x[idx], y[idx], 'ro')

plt.savefig("fig3.png")