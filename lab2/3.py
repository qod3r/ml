import numpy as np


a1 = np.array(list(map(int, input("a1: ").split())))
b1 = np.array([int(input("b1: "))])
a2 = np.array(list(map(int, input("a2: ").split())))
b2 = np.array([int(input("b2: "))])

a = np.concatenate([a1, a2]).reshape([2, 2])
b = np.concatenate([b1, b2])
# print(a, b)

if np.linalg.det(a) != 0:
    x = np.linalg.solve(a, b)
    if np.allclose(np.dot(a, x), b):
        print(f"solution: {x}")
else:
    print("no solutiuons")