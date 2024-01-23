def write_string(lst):
    text = f'Шляпка гриба, покрытая {lst[0]} кожиц{lst[1]}й, держится на {lst[2]} ножк{lst[3]}.\
    Снизу шляпка затянута {lst[4]} пленкой. Когда ее уберешь откроется нижняя {lst[5]} сторона шляпк{lst[6]}.'
    return text
list_of_insertions = ['...', '..', '...', '..', '...', '...', '..']
print(write_string(list_of_insertions))
list_of_insertions[0] = input('введите недостающее слово: покрытая ...')
list_of_insertions[1] = input('введите недостающую букву: кожиц..')
list_of_insertions[2] = input('введите недостающее слово: держится на ...')
list_of_insertions[3] = input('введите недостающую букву: ножк..')
list_of_insertions[4] = input('введите недостающее слово: затянута ...')
list_of_insertions[5] = input('введите недостающее слово: нижняя ...')
list_of_insertions[6] = input('введите недостающую букву: шляпк..')

print(write_string(list_of_insertions))