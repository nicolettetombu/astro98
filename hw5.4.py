import numpy as  np

np.random.seed(12345)
a = np.random.randint(1,50, (4,5))

sortedMatrix = np.sort(a, axis = 0)

print(sortedMatrix)
