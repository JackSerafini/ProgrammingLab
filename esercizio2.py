from datetime import datetime 

def lettura_date():
    my_file = open('shampoo_sales.csv', 'r')
    dates = []
    for line in my_file:
        tmp = line.split(',')
        if tmp[0] != 'Date':
            data = datetime.strptime(tmp[0], '%d-%m-%Y')
            dates.append(data)
    my_file.close()
    return dates

date_vendite = lettura_date()
for data in date_vendite:
    print(data.strftime('%d-%m-%Y'))