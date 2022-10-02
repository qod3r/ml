import numpy as np
from numpy.polynomial import Polynomial


# 1
a1 = [1, 2, 3, 4, 5]
a2 =          [4, 5, 6, 7, 8]
print("\n1.")
print(a1, a2)
print(np.intersect1d(a1, a2))

# 2
print("\n2.")
a = [1, 2, 3, 4, 3, 2, 1]
print(a)
print(np.unique(a))

# 3
a = [1, 2, 3, 4, 3, 2, 1]
uniq, counts = np.unique(a, return_counts=True)
print("\n3.")
print(a)
print(f"unique: {uniq}\ncounts: {counts}")

# 4
a = np.array([1, 2, 3, 4])
print("\n4.")
print(a)
print(np.concatenate([a, a]))

# 5
a = np.array([1, 2, 3, np.nan, 1, np.nan, 2])
print("\n5.")
print(a)
print(a[~np.isnan(a)])

# 6
a = np.array([6, 5, 4, 3, 2, 1])
print("\n6.")
print(a)
print(np.sort(a)[:4])

# 7
a = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
val = 3.09066280756759
print("\n7.")
print(a, val)
print(a[(np.abs(a - val)).argmin()])

# 8
a1 = np.array(['Python', 'PHP'])
a2 = np.array(['Java', 'C ++'])
print("\n8.")
print(a1, a2)
print(np.core.defchararray.add(a1, a2))

# 9
a = ['Python', 'PHP', 'JS', ' examples', 'html']
v = np.vectorize(lambda s: s.count('P'))
print("\n9.")
print(a)
print(v(a))

# 10
print("\n10.")
p1 = Polynomial([1, -4, 7])
print("p1: x^2 - 4x + 7")
print("x: ", p1.roots())
p2 = Polynomial([1, -11, 9, 11, -10])
print("p2: x^4 - 11x^3 + 9x^2 + 11x - 10")
print("x: ", p2.roots())