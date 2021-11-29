def leggere(lista):
    for element in lista:
        print(element)
    print(lista)

def statistiche(lista):
    numero_elementi = 0
    if type(lista) == list:
        somma = sum(lista)
        media = sum(lista)/len(lista)
        minimo = min(lista)
        massimo = max(lista)

    print('Somma = {}'.format(somma))
    print('Media = {}'.format(media))
    print('Massimo = {}'.format(massimo))
    print('Minimo = {}'.format(minimo))

def somma_vettoriale(lista1, lista2):
    lista3 = []
    if type(lista1) == type(lista2) == list and len(lista1) == len(lista2):
        lista3 = lista1 + lista2
        return lista3

    else:
        lista4 = []
        return lista4

my_list = [2, 6, 24, 1, 98]
#leggere(my_list)
#statistiche(my_list)
listas = [12, 4, 21, 6, 74, 12]
listass = [2, 5, 7, 22, 65]
print(somma_vettoriale(listas, listass))