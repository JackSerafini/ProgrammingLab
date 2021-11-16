def somma(lista):
    my_var = 0
    for item in lista:
        my_var = my_var + item
    return my_var


lista = [1, 4, 2, 8, 4]
print('Somma: {}'.format(somma(lista)))  