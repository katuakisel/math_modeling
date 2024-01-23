from block_3_const import g_earth

def get_energy(h, m):
    E_full = m * g_earth * h
    print(f'Полная энергия тела массой {m} кг, подброшенное на высоту {h}м над поверхностью земли равна Еп = {E_full}Дж')
    return


h= float(input('Введите высоту, в метрах, на которое подброшено тело над поверхностью земли h= '))
m= float(input('Введите массу тела m= '))
get_energy(h, m)