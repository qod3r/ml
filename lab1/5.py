import matplotlib.pyplot as plt
import numpy as np


figures = []
language_data = {
    "Java": 22.2,
    "Python": 17.6,
    "PHP": 8.8,
    "JavaScript": 8,
    "C#": 7.7,
    "C++": 6.7
}

# 1
fig = plt.figure(0)

plt.bar(language_data.keys(), language_data.values(), color='blue')
plt.minorticks_on()
plt.grid(which='major', c='r', linestyle='-')
plt.grid(which='minor', c='black', linestyle='dotted')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming languages\nworldwide, oct 2017 compared to a year ago")
figures.append(fig)

# 2
fig = plt.figure(1)

plt.barh(list(language_data.keys()), language_data.values(), color='green')
plt.minorticks_on()
plt.grid(which='major', c='r', linestyle='-')
plt.grid(which='minor', c='black', linestyle='dotted')
plt.ylabel("Languages")
plt.xlabel("Popularity")
plt.title("Popularity of programming languages\nworldwide, oct 2017 compared to a year ago")
figures.append(fig)

# 3
fig = plt.figure(2)

colors = ['r', 'black', 'g', 'b', 'y', 'cyan']
plt.bar(language_data.keys(), language_data.values(), color=colors)
plt.minorticks_on()
plt.grid(which='major', c='r', linestyle='-')
plt.grid(which='minor', c='black', linestyle='dotted')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming languages\nworldwide, oct 2017 compared to a year ago")
figures.append(fig)

# 4
fig = plt.figure(3)

plt.bar_label(plt.bar(language_data.keys(), language_data.values(), color='blue'))
plt.minorticks_on()
plt.grid(which='major', c='r', linestyle='-')
plt.grid(which='minor', c='black', linestyle='dotted')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming languages\nworldwide, oct 2017 compared to a year ago")
figures.append(fig)

# 5
fig = plt.figure(4)
w = [0.1, 0.2, 0.4, 1.1, 0.2, 0.3]
plt.bar(language_data.keys(), language_data.values(), color='blue', width=w)
plt.minorticks_on()
plt.grid(which='major', c='r', linestyle='-')
plt.grid(which='minor', c='black', linestyle='dotted')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming languages\nworldwide, oct 2017 compared to a year ago")
figures.append(fig)

# 6
fig = plt.figure(5)
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
w = [25, 34, 30, 35, 27]
m = [20, 32, 34, 20, 25]
x = np.arange(len(labels))
width = 0.35
plt.bar(x - width/2, m, width, label='Men', color='g')
plt.bar(x + width/2, w, width, label='Women', color='r')
plt.legend()
plt.xlabel('person')
plt.ylabel('scores')
plt.title('scores by person')
figures.append(fig)

# 7
fig = plt.figure(6)

y = list(language_data.values())/np.sum(list(language_data.values()))
plt.pie(y, labels=language_data.keys(), explode=[0.2, 0, 0, 0, 0, 0])
figures.append(fig)

# 8
fig = plt.figure(7)

y = list(language_data.values())/np.sum(list(language_data.values()))
plt.pie(y, labels=language_data.keys(), explode=[0.2, 0.1, 0, 0, 0, 0])
plt.title("Popularity of programming languages\nworldwide, oct 2017 compared to a year ago")
figures.append(fig)


for i in range(len(figures)):
    plt.figure(i)
    plt.savefig(f"fig5-{i+1}.png")