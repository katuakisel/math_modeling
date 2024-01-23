import numpy as np


def get_multiplication(one_d_array):
    rez = 1
    for elem in one_d_array:
        rez *= elem
    return rez

array = np.array([11,2,15], dtype=int)

rez = get_multiplication(array)
print(rez)