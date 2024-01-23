import numpy as np

def get_eval_func(a, b, n):
    # вычисляет функцию в интервале a < x < b для n-точек
    delta_points = (b - a)/(n + 1)
    points = []
    pt_x = a
    for index in range(n):
        pt_x += delta_points
        y_x = pt_x ** 2
        points.append(y_x)

    return points

print(get_eval_func(1, 8, 5))
    