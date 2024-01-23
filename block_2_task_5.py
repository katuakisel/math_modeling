a = int(input('введите первое число: '))
b = int(input('введите второе число: '))

if b != 0:
    rez = a/b
    ost = a % b
    chast = a // b
    if ost != 0:
        print('a не делится без остатка на b: ', rez, ost, chast, end=' ')
    else:
        print('a делится без остатка на b: ', int(rez), chast, end=' ')
else:
    print('Делить на ноль нельзя')