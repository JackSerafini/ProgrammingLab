class CSVFile():
    def __init__(self, name):
        self.name = name
    
#aprire il file e tornare i dati dal file CSV come lista di liste
    def get_data(self):
        
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            print('Non esiste alcun file con quel nome, ho ricevuto questo errore: {}'.format(e))
            exit()

        lista = []
        for line in my_file:
            elements = line.split(',')
            lista.append(elements)
        my_file.close()
        return lista

class NumericalCSVFile(CSVFile):
    def __init__(self, name):
        try:
            f = open(name, 'r')
        except FileNotFoundError as e:
            print(e)
            exit()
        else:
            f.close()
            self.name = name
    
    def data_column(self):
        my_file = open(self.name, 'r')
        lista = []
        final_list = []
        for line in my_file:
            elements = line.split(',')
            for index in range(1, len(elements)):
                if elements[0] != 'Date':
                    lista.append(elements[index].rstrip('\n'))
        for element in lista:
            try:
                final_list.append(float(element))
            except ValueError as e:
                print(e)
                exit()
        return final_list

my_var = NumericalCSVFile('shampoo_sales.csv')
print(my_var.data_column())