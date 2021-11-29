class CSVFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):

        try:
            lista = []
            my_file = open(self.name, 'r')
            for line in my_file:
                elements = line.split(',')
                lista.append(elements)
            my_file.close()
        
            return lista

        except:
            print('Il file non esiste!')

class NumericalCSVFile(CSVFile):
    def __init__(self, name):
        self.name = name

    def text_to_num(self):
        my_file = open(self.name, 'r')
        my_list = []
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                Date = elements[0]
                Value = elements[1]
                my_list.append(float(Value))
        my_file.close()
        
        return my_list

my_var = NumericalCSVFile('shampoo_sales.csv')
print(my_var.text_to_num())