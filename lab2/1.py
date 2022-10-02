import numpy as np


# 1
a = np.array([1, 7, 13, 105])
# print(a.nbytes)
np.savetxt("arr1.txt", a)
np.save("arr1.npy", a)
# print(np.load("arr1.npy"))

# 2
np.zeros([10])
np.ones([10])
np.ones([10])*5

# 3 
np.arange(30, 71, 2)

# 4
np.arange(5, 51, 5)

# 5
np.random.randint(1, 101, [3, 3, 3])

# 6
np.arange(30, 42, 1).reshape([3, 4])

# 7
sq = np.zeros([10, 10])
sq[[0, 9], :] = 1
sq[:, [0, 9]] = 1
# print(sq)

# 8
a = np.zeros([5, 5])
np.fill_diagonal(a, np.arange(1, 6, 1))
# print(a)

# 9
a = np.zeros([4, 4])
a = a.flatten()
a[::2] = 1
a = a.reshape([4, 4])
print(a)

# 10
