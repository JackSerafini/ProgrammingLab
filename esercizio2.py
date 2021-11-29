from datetime import datetime

def lettura_date():
    my_file = open('shampoo_sales.csv', 'r')
    lista = []
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            lista_delle_date = datetime.strptime(elements[0], '%d-%m-%Y')
            lista.append(lista_delle_date)
    
    my_file.close()
    return lista

date_finali = lettura_date()
print('Dates:\n')
for data in date_finali:
    print(data.strftime('%d-%m-%Y'))