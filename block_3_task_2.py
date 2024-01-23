import numpy as np
import block_3_const as const

h = 100
alpha = np.pi / 3
beta = 30 
g = const.g_earth

v = ((g * h * (np.tan(beta * np.pi / 180) ** 2))/(2 * (np.cos(alpha) ** 2) * (1 - np.tan(beta * np.pi / 180)* np.tan(alpha)))) ** 0.5
print('v= ', v)
# print(np.e)

T = 200
epsilon = 300

N = (2 / np.pi) * (const.h_p_plank / (const.k_bol * T) ** (3 / 2)) * (np.e **(- epsilon / (const.k_bol * T))) * (epsilon ** (T / 2))
print('N= ', N)
print(np.e **(-epsilon / (const.k_bol * T)))
print(epsilon ** (T / 2))