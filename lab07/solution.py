import numpy as np

def reshape_rows(values, width):
    arr = np.array(values)
    matrix = arr.reshape(-1,width)
    return matrix.tolist()


def block(matrix, rows, columns):
    arr = np.array(matrix)
    result = arr[np.ix_(rows , columns)]
    return sesult.tolist()
def column_means(matrix):
    arr = np.array(matrix)
    if arr.size == 0:
        return []
    means = np.mean(arr , axis = 0)
    return [round(float(x) , 6)for x in means]
def column_range(matrix, column):
    arr = np.array(matrix)
    if arr.size == 0:
        return 0.0
    values = arr[: , column]
    result = np.max(values) - np.min(values)
    return round(float(result),6)
