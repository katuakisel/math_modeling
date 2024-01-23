from block_3_const import g_earth
from pprint import pprint
time = [0,1,2,3,4,5]

list_b = []
x_0 = 10
v_0 = 25
y_0 = 5 
for t in time:
    list_a = []
    x = x_0 + v_0 * t 
    y = round(y_0 + v_0 * t - g_earth * (t**2)/2, 2)
    list_a.append(t)
    list_a.append(x)
    list_a.append(y)
    print(list_a)
    list_b.append(list_a)
    #print(x, y)

#for list in list_b:
    #print(list)
