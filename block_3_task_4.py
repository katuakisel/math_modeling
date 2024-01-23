import numpy as np

def eval(i, j, n, m):
    rez =  np.sin(n * i + m * j + 1)
    if rez < 0:
        return 0
    else:
        return rez


def create_array(n,m):
    arr_list = []
    for i in range(n):
        row_list = []
        for j in range(m):
            row_list.append(eval(i,j,n,m))
        arr_list.append(row_list)
    return np.array(arr_list)     
    # return np.array([eval(i,j,n,m) for i in range(n) for j in range(m)]).reshape((n,m))

# def create_array(n,m):
#     return np.array([eval(i,j,n,m) for i in range(n) for j in range(m)]).reshape((n,m))

if __name__ == '__main__':
    arr = create_array(4,4)
    print(arr)

