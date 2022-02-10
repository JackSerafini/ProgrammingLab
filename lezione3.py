#funzione che somma tutte le vendite
def somma():
    values = []
    somma = 0
    my_file = open('shampoo_sales.csv', 'r')
    #dividere la data dalle vendite
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            dates = elements[0]
            value = elements[1]

            #creare una liste delle vendite
            values.append(float(value))
    #sommo tutti i valori
    for value in values:
        somma = somma + value
    return somma

print(somma())