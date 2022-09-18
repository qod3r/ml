import matplotlib.pyplot as plt
import numpy as np

figures = []


# 1
func1 = lambda x: x * 2

fig1 = plt.figure(1)
plt.plot([x for x in range(50)], [func1(x) for x in range(50)])
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Draw a line.")
figures.append(fig1)


# 2
func2 = lambda x: -abs(x - 20) + 20

fig2 = plt.figure(2)
ax = fig2.add_subplot()
ax.plot([x for x in range(50)], [func2(x) for x in range(50)], label="line1-width5", linewidth=5)
ax.plot([x for x in range(50)], [-func2(x)+5 for x in range(50)], label="line2-width2", linewidth=2)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Two or more lines with different widths and colors with suitable legends")
plt.legend()
figures.append(fig2)


# 3
fig3 = plt.figure(3)
ax = fig3.add_subplot()
ax.plot([x for x in range(50)], [func2(x) for x in range(50)], ':', label="line1-dotted", linewidth=5)
ax.plot([x for x in range(50)], [-func2(x)+5 for x in range(50)], '--',label="line2-dashed", linewidth=2)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Plot with two or more lines with different styles")
plt.legend()
figures.append(fig3)


# 4
fig4 = plt.figure(4)
ax = fig4.add_subplot()
ax.plot([1, 4, 5, 6, 7], [2, 6, 3, 6, 3], 'r-.', marker='o', markerfacecolor='blue', markersize=10)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Display marker")
figures.append(fig4)


# 5
fig5 = plt.figure(5)
ax = fig5.add_subplot()
ax.scatter([2, 3, 5, 6, 8], [1, 5, 10, 18, 20], linewidths=0.5, marker='*', c='blue')
ax.scatter([3, 4, 6, 7, 9], [2, 6, 11, 20, 22], linewidths=3, c='red')
ax.set_xlim(xmin=0)
figures.append(fig5)


# 6
fig6 = plt.figure(6)
ax = fig6.add_subplot()
data = {
    "2016-10-03": 772.5,
    "2016-10-04": 776.42,
    "2016-10-05": 776.49,
    "2016-10-06": 776.85,
    "2016-10-07": 775.09
}
ax.plot(data.keys(), data.values(), c='r', marker='o')
plt.minorticks_on()
ax.grid(color='r', linestyle='-', which="major", linewidth=0.75)
ax.grid(color='black', linestyle='dotted', which="minor", linewidth=0.7)

ax.set_yticks(np.arange(772, 777, 0.5))
plt.xlabel("Date")
plt.ylabel("Closing value")
plt.title("Closing stock value of Alphabet Inc.")
figures.append(fig6)


for i in range(len(figures)):
    plt.figure(i + 1)
    plt.savefig(f"fig1-{i + 1}.png")