import numpy as np

ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
ls3 = ls1 + ls2
print(ls3)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = arr1 + arr2
print(arr3)

def loopSum():
    sum = 0
    for i in range(101):
        sum += i
    return sum 
print(loopSum())

def arraySum():
    x = np.arange(101)
    y = np.sum(x)
    return y 
print(arraySum())