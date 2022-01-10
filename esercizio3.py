class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista = []
        my_file = open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            lista.append(elements)
        my_file.close()
        return lista

    def get_date_vendite(self):
        my_file = open('shampoo_sales.csv', 'r')
        dates = []
        for line in my_file:
            tmp = line.split(',')
            if tmp[0] != 'Date':
                data = datetime.strptime(tmp[0], '%d-%m-%Y')
                dates.append(data)
        my_file.close()
        return dates

    def __str__(self):
        my_file = open(self.name, 'r')
        header = my_file.readline()
        my_file.close()
        return header

my_var = CSVFile('shampoo_sales.csv')
print(my_var.__str__())