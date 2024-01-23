b_1 = int(input('Введите первый элемент последовательности: '))
q = int(input('Введите знаменатель: '))
n = int(input('Введите количество членов прогрессии: '))
# b_n = b_1 * q ** (n - 1)
for index in range(1, n+1):
    # print(index)
    b_n = b_1 * q ** (index - 1)
    print(b_n, end=' ')
# print(b_n)