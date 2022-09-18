import matplotlib.pyplot as plt
import numpy as np


figures = []

# 1
fig = plt.figure(0)

x = list(range(9))
y = [0, 0, 0.3, 0.025, 0.18, 0.27, 0.08, 0, 0]
plt.bar(x, y, color='pink')

figures.append(fig)




for i in range(len(figures)):
    plt.figure(i)
    plt.savefig(f"fig6-{i+1}.png")