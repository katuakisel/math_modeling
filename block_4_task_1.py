import numpy as np


def get_average(one_d_array):
    rez = 0
    for elem in one_d_array:
        rez += elem
    return rez / len(one_d_array)

array = np.array([10,2,15])

rez = get_average(array)
print(rez)