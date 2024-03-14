import numpy as np

arr = np.array([[1,1,1], [1,2,3],[2,2,2]])
def findrows(arr):
    equal_rows = []
    for row in arr:
        if all(element == row[0] for element in row):
            equal_rows.append(row)
    return equal_rows 

print(findrows(arr))
