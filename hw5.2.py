import numpy as np

array = np.zeros((8,8), dtype=int)
array[::2, ::2] = 1
array[1::2, 1::2] = 1

print(array)